"""Test all five required emotion examples against the live Watson API."""
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Validate each required dominant emotion."""
    def test_required_emotions(self):
        """Check five statements using separately reported subtests."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(emotion_detector(text)["dominant_emotion"], expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
