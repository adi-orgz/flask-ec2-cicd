import pytest
from app import app as flask_app

@pytest.fixture(autouse=True)
def _setup_test_reporting(request):
    """Setup for test reporting"""
    request.node.test_result = "❌"  # Default to failed

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Update test results for reporting"""
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if result.passed:
            item.test_result = "✅"
        elif result.failed:
            item.test_result = "❌"
        elif result.skipped:
            item.test_result = "⚠️"