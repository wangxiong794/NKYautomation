# coding=utf-8
from unittest import TestCase
from unittest.case import TestCase
import time
from unittest import case

class TestCase_(TestCase):
    # 是否开启失败重跑
    FAILURE_REPEAT_RUN_FLAG = False
    # 失败重跑尝试次数
    FAILURE_REPEAT_RUN_NUM = 3
    # 设置重跑时间间隔
    REPEAT_TIME_INTERVAL = 5

    def run(self, result=None):
        run_count = 1
        orig_result = result
        result.succeed_failure_error_flag = None
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
        result.startTest(self)
        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
                getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, self, skip_why)
            finally:
                result.stopTest(self)
            return
        expecting_failure_method = getattr(testMethod,
                                           "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self,
                                          "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method

        try:
            while True:
                outcome = _Outcome(result)
                self._outcome = outcome
                with outcome.testPartExecutor(self):
                    self.setUp()
                if outcome.success:
                    outcome.expecting_failure = expecting_failure
                    with outcome.testPartExecutor(self, isTest=True):
                        testMethod()
                    outcome.expecting_failure = False
                    with outcome.testPartExecutor(self):
                        self.tearDown()
                self.doCleanups()
                # 跳过执行的在这里记录
                for test, reason in outcome.skipped:
                    self._addSkip(result, test, reason)
                # 执行测试过程中，raise的非（skiptest以及期望失败）异常--即测试失败，在这里处理到结果中
                self._feedErrorsToResult(result, outcome.errors)
                # outcome.success
                # raise skiptest异常时 outcome.success =false
                # 当期望测试执行失败时即expecting_failure=true， outcome.success =true
                # raise 异常时（不管是不是AssertionError） outcome.success =false
                #
                if outcome.success:
                    if expecting_failure:
                        if outcome.expectedFailure:
                            self._addExpectedFailure(result, outcome.expectedFailure)
                        else:
                            self._addUnexpectedSuccess(result)
                    else:
                        result.addSuccess(self)
                # ================重跑======================
                if not self.FAILURE_REPEAT_RUN_FLAG:
                    return result
                if run_count < self.FAILURE_REPEAT_RUN_NUM:
                    if (not outcome.success) and len([error for error in outcome.errors if error[1] is not None]) > 0:
                        try:
                            last_test_result = result.result[-1][0]
                        except Exception as e:
                            pass
                        else:
                            try:
                                if last_test_result == 1:
                                    result.failures.pop()
                                    result.result.pop()
                                    result.failure_count -= 1
                                    run_count += 1
                                    time.sleep(self.REPEAT_TIME_INTERVAL)
                                    continue
                                elif last_test_result == 2:
                                    result.errors.pop()
                                    result.result.pop()
                                    result.error_count -= 1
                                    run_count += 1
                                    time.sleep(self.REPEAT_TIME_INTERVAL)
                                    continue
                                else:
                                    pass
                            except Exception as e:
                                pass

                # ============================================================
                return result

        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()

            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None

            # clear the outcome, no more needed
            self._outcome = None
