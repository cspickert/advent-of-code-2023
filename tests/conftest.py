import pytest
from pathlib import Path
from run import Runner


@pytest.fixture
def run_part(request):
    def fn():
        day_module = str(request.function.__module__).split("_")[-1]
        part_name = request.function.__name__.split("_")[-1]
        input_path = Path(__file__).parent / "input" / day_module / f"{part_name}.txt"
        runner = Runner(day_module, input_path)
        return runner.run_method(part_name)

    return fn
