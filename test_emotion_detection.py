from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        tests = [
            ['I am glad this happened', 'joy'],
            ['I am really mad about this', 'anger'],
            ['I feel disgusted just hearing about this', 'disgust'],
            ['I am so sad about this', 'sadness'],
            ['I am really afraid that this will happen', 'fear'],
        ]

        for statement, expected in tests:
            result = emotion_detector(statement)
            self.assertEqual(result['dominant_emotion'], expected)


unittest.main()
