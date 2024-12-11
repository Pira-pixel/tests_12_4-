import unittest
import logging
from pythonProject.Lessons.Module12.tests_12_2.tests.runner import Runner


# Настройка логирования


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner('Den', speed=-5)  # Передаем отрицательное значение в speed
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:  # Предполагаем, что Runner выбрасывает ValueError для неверной скорости
            logging.warning("Неверная скорость для Runner: %s", e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(123, speed=10)  # Передаем что-то кроме строки в name
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:  # Предполагаем, что Runner выбрасывает TypeError для неверного типа данных
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner('Den')
        runner2 = Runner('Max')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='runner_tests.log',
        format='%(asctime)s | %(levelname)s | %(message)s',
        encoding='utf-8'
    )
