# The unittest library will be used to test the emotion_detector functionality.
import unittest

# Import the function to be tested.
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for dominant emotion: joy
        test_1 = emotion_detector("I am glad this happened")
        self.assertEqual(test_1['dominant_emotion'],'joy')

        # Test case for dominant emotion: anger
        test_2 = emotion_detector("I am really mad about this")
        self.assertEqual(test_2['dominant_emotion'],'anger')

        # Test case for dominant emotion: disgust
        test_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_3['dominant_emotion'],'disgust')

        # Test case for dominant emotion: sadness
        test_4 = emotion_detector("I am so sad about this")
        self.assertEqual(test_4['dominant_emotion'],'sadness')

        # Test case for dominant emotion: fear
        test_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_5['dominant_emotion'],'fear')

if __name__ == '__main__':
    unittest.main()

