import api
import exceptions

import unittest


class TestCreateQuery(unittest.TestCase):

    def test_create_query(self):
        test_language = ["Python", "Ruby", "Java"]
        test_min_stars = 10000

        expected = "Language: Python Language: Ruby Language: Java stars:>10000"
        result = api.create_query(test_language, test_min_stars)

        self.assertEqual(result, expected,
                         "Unexpected result from create_query")


class TestGithubApiError(unittest.TestCase):

    def test_exception_403(self):
        status_code = 403
        exception = exceptions.GitHubApiError(status_code=status_code)
        self.assertTrue("Rate limit" in str(
            exception), "'Rate limit' not found")

    def test_exception_500(self):
        status_code = 500
        exception = exceptions.GitHubApiError(status_code=status_code)
        self.assertTrue(status_code) in str(exception)


if __name__ == "__main__":
    unittest
