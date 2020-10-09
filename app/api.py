from functools import partial
from time import time
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

from flask import Flask, request, jsonify

app = Flask(__name__)

DEFAULT_TIMEOUT = 60


def load_creator_helper(timeout: int, arg: int) -> None:
    """
    Runs a cpu intensive task for a number of seconds.

    :param timeout: int - after how long the worker should timeout
    :param arg: an int that will be the power of itself
    :return:
    """
    start_time = time()
    while time() - start_time < timeout:
        arg ** arg


def cpu_load_creator(timeout: int) -> None:
    """
    Spawns a N an amount of load_creator_helper workers, where N is the number of cpu cores.

    :param timeout: int - after how long each worker should time out
    :return: None
    """
    processor_core_count = cpu_count()
    with ProcessPoolExecutor(max_workers=processor_core_count) as executor:
        # partial is used to set the timeout arg of the load_creator_helper function
        executor.map(partial(load_creator_helper, timeout), range(processor_core_count))


@app.route('/')
def hello_world():
    """Prints greeting"""
    return 'Hello World'


@app.route('/intense', methods=['GET', 'POST'])
def execute_intense_task():
    """
    Runs a CPU intense task for 60 seconds or the specified number of seconds in the API endpoint request like
    host:port/intense?timeout=N

    :return: a json structure
    """
    timeout = int(request.args.get('timeout', DEFAULT_TIMEOUT))
    cpu_load_creator(timeout=timeout)
    return jsonify({'status': 'success', 'timeout': timeout})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
