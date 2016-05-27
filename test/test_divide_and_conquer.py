import divide_and_conquer.binary_search as binary_search
import divide_and_conquer.inversions as inversions
import divide_and_conquer.majority_element as majority_element
import divide_and_conquer.points_and_segments as points_and_segments
import divide_and_conquer.sorting as sorting
import pytest


@pytest.mark.timeout(10)  # 10 seconds timeout for binary this tests
class TestBinarySearch:
    @pytest.mark.parametrize("test_input,expected", [
        (([5, 1, 5, 8, 12, 13], [5, 8, 1, 23, 1, 11]), "2 0 -1 0 -1")
    ])
    def test_sample(self, test_input, expected, main_runner):
        assert expected in main_runner(binary_search, test_input)

    def test_worst_case(self):
        a = [i for i in range(10 ** 5)]
        assert len(a) - 1 == binary_search.binary_search(a, a[-1])

    def test_middle_element_even(self):
        a = [i for i in range(10 ** 5)]
        assert len(a) // 2 == binary_search.binary_search(a, a[len(a) // 2])

    def test_middle_element_odd(self):
        a = [i for i in range(10 ** 5 - 1)]
        assert len(a) // 2 == binary_search.binary_search(a, a[len(a) // 2])

    def test_worst_problem_size(self):
        a = [i for i in range(10 ** 5)]
        for x in range(len(a), len(a) + 10 ** 5):
            assert -1 == binary_search.binary_search(a, x)

    def test_2_grader(self, main_runner):
        test_input = ([10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                      [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        expected = "-1 0 1 2 3 4 5 6 7 8 9 -1"
        assert expected in main_runner(binary_search, test_input)


@pytest.mark.skip(reason="Working with Binary search first")
class TestInversions:
    @pytest.mark.parametrize("test_input,expected", [
        (([5], [2, 3, 9, 2, 2]), "1"),
        (([4], [1, 2, 3, 4]), "0"),
        (([4], [1, 2, 3, 1]), "0")
    ])
    def test_samples(self, test_input, expected, main_runner):
        assert expected in main_runner(inversions, test_input)


@pytest.mark.skip(reason="Not paassing on graaader yet")
class TestMajorityElement:
    @pytest.mark.parametrize("test_input,expected", [
        (([5], [2, 3, 9, 2, 2]), "1"),
        (([4], [1, 2, 3, 4]), "0"),
        (([4], [1, 2, 3, 1]), "0")
    ])
    def test_sample(self, test_input, expected, main_runner):
        assert expected in main_runner(majority_element, test_input)


@pytest.mark.skip(reason="TODO")
class TestPointsAndSegments:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(3, [1, 6], [2, 5], [3, 6])
        points_and_segments.main()
        out, err = capfd.readouterr()
        assert "1\n3" in out


@pytest.mark.skip(reason="TODO")
class TestSorting:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(6)
        sorting.main()
        out, err = capfd.readouterr()
        assert "3\n1 2 3" in out
