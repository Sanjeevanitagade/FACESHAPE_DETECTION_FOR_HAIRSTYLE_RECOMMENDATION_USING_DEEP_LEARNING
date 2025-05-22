import cv2
import dlib
import numpy as np
import os

def load_dlib_model():
    # Load dlib face detector and shape predictor
    try:
        face_detector = dlib.get_frontal_face_detector()
        landmark_predictor = dlib.shape_predictor('../models/shape_predictor_68_face_landmarks.dat') # Replace with your model path.
        return face_detector, landmark_predictor
    except Exception as e:
        print(f"Error loading dlib model: {e}")
        return None, None

def detect_face_and_landmarks(image, face_detector, landmark_predictor):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray)
        if not faces:
            return None, None,None
        face = faces[0]
        landmarks = landmark_predictor(gray, face)

        landmarks_list = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_list.append((x,y))
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
        x_start, y_start, x_end, y_end = face.left(), face.top(),face.right(), face.bottom()
        return image, landmarks_list, (x_start, y_start, x_end, y_end)
    except Exception as e:
        print(f"Error detecting face and landmarks: {e}")
        return None, None, None

def get_hairstyle_recommendations(face_shape):
    try:
        hairstyle_data = {
            "oval": {
                "hairstyles": [
                    {"name": "Beachy Face-Framing Layers", "description": "Beachy Face-Framing Layers: Effortlessly tousled layers that frame the face for a relaxed, beachy vibe.", "image": "/images/Beachy Face-Framing Layers.png"},
                    {"name": "Center-Parted Curls", "description": "Soft, voluminous curls parted down the center for a balanced, natural look.", "image": "/images/Center-Parted Curls.png"},
                    {"name": "Full Fringe", "description": "Bold, straight-across bangs that create a dramatic and youthful appearance.", "image": "/images/Full Fringe.png"},
                    {"name": "Long and Wavy", "description": "Flowing waves that add volume and texture to long hair for a carefree, beachy style.", "image": "/images/Long and Wavy.png"},
                    {"name": "Shoulder-Length Soft Curls", "description": "Gentle curls at shoulder length for a soft, feminine, and polished look.", "image": "/images/Shoulder-Length Soft Curls.png"},
                    {"name": "Subtle Side-Swept", "description": "Lightly swept bangs to the side for a soft and sophisticated effect.", "image": "/images/Subtle Side-Swept.png"},
                    {"name": "Wispy Long Bob", "description": "A modern, textured bob with wispy ends for a chic and effortless style.", "image": "/images/Wispy Long Bob.png"},
                    {"name": "Retro Waves", "description": "Vintage-inspired waves that evoke glamour and timeless elegance.", "image": "/images/Retro Waves.png"},
                    {"name": "Polished Curls", "description": " Well-defined, shiny curls that add a touch of sophistication and style.", "image": "/images/Polished Curls.png"},
                    {"name": "Angled Lob", "description": "A sleek, angular bob that creates a sharp, contemporary silhouette.", "image": "/images/Angled Lob.png"}
                ]
            },
            "heart": {
                "hairstyles": [
                    {"name": "Wavy Lob with a Center Part", "description": "A textured lob with soft waves and a center part for a laid-back yet stylish look.", "image": "/images/Wavy Lob with a Center Part.png"},
                    {"name": "Blunt Bangs", "description": "Straight-across bangs that add a bold and edgy touch to any hairstyle.", "image": "/images/Blunt Bangs.png"},
                    {"name": "Bouncy Curls", "description": "Lively, voluminous curls that create a playful and energetic vibe.", "image": "/images/Bouncy Curls.png"},
                    {"name": "Curly Shag", "description": "A shaggy cut with layers and defined curls for a messy, textured finish.", "image": "/images/Curly Shag.png"},
                    {"name": "Flared Bob", "description": "A chic bob that gently flares out at the ends, offering a retro-inspired silhouette.", "image": "/images/Flared Bob.png"},
                    {"name": "Middle Part Blonde Hair", "description": "A classic, sleek look with blonde hair parted down the middle for balance and simplicity.", "image": "/images/Middle Part Blonde Hair.png"},
                    {"name": "Long Layered Lob", "description": "A long lob with layers for added movement and dimension.", "image": "/images/Long Layered Lob.png"},
                    {"name": "Top Bun with Bangs", "description": "A trendy top bun paired with bangs for a cute and effortless style.", "image": "/images/Top Bun with Bangs.png"},
                    {"name": "Side-Swept Bangs", "description": "Soft bangs swept to the side for a flattering, elegant look.", "image": "/images/Side-Swept Bangs.png"},
                    {"name": "Side Sweeping", "description": "A subtle, flowing style with hair gently swept to the side for a soft, romantic feel.", "image": "/images/Side sweeping.png"}
                ]
            },
            "square": {
                "hairstyles": [
                    {"name": "Long Layered Haircut for Straight Hair", "description": "Sleek long layers that add movement and texture to straight hair.", "image": "/images/Long Layered Haircut For Straight Hair.png"},
                    {"name": "Diamond Cut", "description": "Angled cut that creates a flattering, face-framing shape with added volume.", "image": "/images/Diamond Cut.png"},
                    {"name": "Curtain Bangs", "description": "Soft, parted bangs that frame the face with a relaxed, elegant feel.", "image": "/images/Curtain Bangs.png"},
                    {"name": "Classic Long Bob", "description": "A timeless bob that hits just above the shoulders for a polished look.", "image": "/images/Classic Long Bob.png"},
                    {"name": "A Weightless Cut", "description": "Light, airy layers that add natural movement and volume to the hair.", "image": "/images/A Weightless Cut.png"},
                    {"name": "Long Layered and Curly", "description": "Layers combined with curls for added volume and bounce.", "image": "/images/Long, Layered, And Curly.png"},
                    {"name": "Side Bangs with Layered Hairstyles", "description": "Side-swept bangs paired with layers for a soft, stylish finish.", "image": "/images/Side Bangs With Layered Hairstyles.png"},
                    {"name": "Chic Bob With Side Parting", "description": "A sleek bob with a side part for a sophisticated and refined look.", "image": "/images/Chic Bob With Side Parting.png"},
                    {"name": "The Trailblazer Bob", "description": "A bold, modern bob with edgy angles for a trendy, sharp style.", "image": "/images/The Trailblazer Bob.png"},
                    {"name": "Textured Ponytail", "description": "A voluminous, textured ponytail that adds a dynamic, casual flair.", "image": "/images/Textured Ponytail.png"}
                ]
            },
            "long": {
                "hairstyles": [
                    {"name": "Bouncy Blowout", "description":"A voluminous, smooth blowout that adds lively bounce and shine to the hair.", "image": "/images/Bouncy Blowout.png"},
                    {"name": "Deep Side Part", "description": "A dramatic side part that adds structure and sophistication to any style.", "image": "/images/Deep Side Part.png"},
                    {"name": "Long Retro Waves", "description": "Soft, vintage-inspired waves that add glamour and elegance to long hair.", "image":"/images/Long, Retro Waves.png"},
                    {"name": "Slicked Down", "description": "A sleek, smooth style achieved by combing hair flat for a polished, refined look.", "image": "/images/Slicked Down.png"},
                    {"name": "Short Bob Haircut", "description": "A chic and versatile bob that falls just above the chin for a sharp, modern look.", "image": "/images/Short Bob Haircut.png"},
                    {"name": "Blown Out", "description": "A smooth, voluminous hairstyle achieved with a blow dryer for a polished finish.", "image": "/images/Blown Out.png"},
                    {"name": "Jellyfish Cut", "description": "A layered cut with short layers at the top and longer ones at the bottom for a unique, edgy look.", "image": "/images/Jellyfish Cut.png"},
                    {"name": "Curly Crop", "description": "A short, curly style that adds texture and a playful, edgy vibe", "image": "/images/Curly Crop.png"},
                    {"name": "Asymmetric Lob with Bangs", "description": "A lob with uneven lengths and bangs for a bold, modern appearance.", "image": "/images/Asymmetric Lob With Bangs.png"},
                    {"name": "Choppy Lob with Curtain Bangs", "description": "A textured lob paired with soft curtain bangs for a relaxed, stylish vibe.", "image": "/images/Choppy Lob With Curtain Bangs.png"}
                ]
            },
            "round": {
                "hairstyles": [
                    {"name": "Textured Bob with Center Part", "description": "A choppy bob with a center part for a casual yet edgy vibe.", "image": "/images/Textured Bob With Center Part.png"},
                    {"name": "Sleek Layers", "description": "Smooth, polished layers that add dimension and flow to the hair.", "image": "/images/Sleek Layers.png"},
                    {"name": "Shaggy Medium Length", "description": "A textured, layered cut at medium length for a messy, carefree look.", "image": "/images/Shaggy Medium Length.png"},
                    {"name": "The Ultimate Blowout", "description":  "A voluminous, smooth style with lots of body and shine, achieved with a blow dryer.", "image": "/images/The Ultimate Blowout.png"},
                    {"name": "Half-Up, Half-Down", "description": "A versatile style where half the hair is pulled up, leaving the rest flowing freely.", "image": "/images/Half-Up, Half-Down.png"
                    },
                    {"name": "Sleek Long Hair", "description": "Long, straight, and smooth hair for a polished and refined look.", "image": "/images/Sleek Long Hair.png"},
                    {"name": "Boho-Chic Waves", "description": "Loose, natural waves that give off a free-spirited, bohemian vibe.", "image": "/images/Boho-Chic Waves.png"},
                    {"name": "Cropped Bob with Choppy Ends", "description": "A short, textured bob with edgy, uneven ends for a modern look.", "image": "/images/Cropped Bob with Choppy Ends.png"},
                    {"name": "Mid-Length Curly Hairstyle", "description": "Bouncy, voluminous curls styled at a flattering mid-length for a dynamic appearance.", "image": "/images/Mid-Length Curly Hairstyle.png"}
                ]
            }
        }
        return hairstyle_data.get(face_shape, {"hairstyles": []})
    except Exception as e:
        print(f"Error loading hairstyle recommendation: {e}")
        return {"hairstyles": []}