import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            {
                "text": "I am glad this happened",
                "expected_emotion": "joy"
            },
            {
                "text": "I am really mad about this",
                "expected_emotion": "anger"
            },
            {
                "text": "I feel disgusted just hearing about this",
                "expected_emotion": "disgust"
            },
            {
                "text": "I am so sad about this",
                "expected_emotion": "sadness"
            },
            {
                "text": "I am really afraid that this will happen",
                "expected_emotion": "fear"
            }
        ]

        for test_case in test_cases:
            result = emotion_detector(test_case["text"])
            self.assertEqual(
                result["dominant_emotion"],
                test_case["expected_emotion"],
                f"Expected {test_case['expected_emotion']} for text: '{test_case['text']}'"
            )

if __name__ == "__main__":
    unittest.main()