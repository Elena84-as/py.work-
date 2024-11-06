import runner
from unittest import TestCase, main


class RunnerTest(TestCase):

    def test_walk(self):
        human = runner.Runner(name='')
        for _ in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)

    def test_run(self):
        human = runner.Runner(name='')
        for _ in range(10):
            human.run()
        self.assertEqual(human.distance, 100)

    def test_challenge(self):
        human_w = runner.Runner(name='')
        human_r = runner.Runner(name='')
        for _ in range(10):
            human_r.walk()
            human_w.run()
            self.assertNotEqual(human_w.distance, human_r.distance)



if __name__== '__mane__':
    main()
