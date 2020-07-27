from src.data.data_preprocessing.utils.spacy_helpers import remove_unnecessary_pos, get_lemmatized_text
import re


def replace_emoji_with_text(token):
    positive_emojis = [':smiley:', ':smile:', ':relaxed:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue:', ':heart:',
                      ':two_hearts:', ':simple_smile:', ':heart_eyes:', ':laughing:', ':relieved:', ':grin:', ':kissing_smiling_eyes:',
                      ':purple_heart:', ':green_heart:', ':person_raising_hand:', ':face_savoring_food:',
                       ':chocolate_bar:', ':cherries:', ':pineapple:', ':beaming_face_with_smiling_eyes:',
                       ':smiling_face_with_sunglasses:', ':thumbs_up:', ':face_with_tears_of_joy:', ':bowtie:', ':kissing_closed_eyes:',
                       ':wink:', ':kissing_closed_eyes:', ':sunglasses:', ':purple_heart:', ':heartpulse:',
                       ':+1:', ':punch:', ':clap:', ':smile_cat:', ':smile:', ':relaxed:',
                       ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue:', ':triumph:', ':innocent:', ':heart:',
                       ':two_hearts:', ':star:', ':thumbsup:', ':heart_eyes_cat:',
                       ':joy_cat:', ':simple_smile:', ':smirk:', ':relieved:', ':stuck_out_tongue_closed_eyes:'
                        , ':grimacing:', ':green_heart:', ':revolving_hearts:', ':raised_hands:', ':kissing_cat:'
                        , ':pouting_cat:', ':kiss:', ':tongue:', ':laughing:', ':heart_eyes:', ':satisfied:',
                       ':grinning:', ':yum:', ':smiling_imp:', ':yellow_heart:', ':broken_heart:', ':blush:',
                       ':kissing_heart:', ':grin:', ':kissing:', ':joy:', ':angry:', ':sparkling_heart:',
                       ':blue_heart:', ':ok_hand:', ':wave:', ':snowflake:', ':smiling_face_with_heart-eyes:',
                       ':red_heart:', ':winking_face:', ':waving_hand:', ':grinning_squinting_face:',
                       ':kissing_face_with_smiling_eyes:', ':glowing_star:', ':raising_hands:',
                       ':white_heart:', ':smiling_face_with_3_hearts:', ':bouquet:', ':winking_face_with_tongue:',
                       ':crown:', ':small_blue_diamond:',  ':love-you_gesture:',  ':astonished_face:', ':beer_mug:',
                       ':relieved_face:', ':Statue_of_Liberty:', ':water_wave:', ':star-struck:',
                       ':smiling_face_with_halo:', ':busts_in_silhouette:', ':hundred_points:', ':upside-down_face:',
                       ':smiling_face_with_halo:', ':busts_in_silhouette:', ':folded_hands:', ':money-mouth_face:',
                       ':clown_face:', ':heart_suit:', ':love-you_gesture:', ':clapping_hands:', ':white_medium_star:',
                       ':place_of_worship:', ':beating_heart:', ':rocket:', ':sparkles:', ':nail_polish:',
                       ':crossed_fingers:', ':confetti_ball:', ':rainbow:', ':zany_face:', ':smirking_face:',
                       ':hundred_points:', ':sign_of_the_horns:', ':victory_hand:', ':ferris_wheel:',
                       ':sunrise_over_mountains:', ':shopping_bags:', ':shopping_cart:', ':Santa_Claus:',
                       ':globe_showing_Americas:', ':smiling_cat_face_with_heart-eyes:', ':partying_face:',
                       ':large_blue_diamond:', ':video_game:']

    negative_emojis = [':sleepy_face:', ':frowning:', ':unamused:', ':fearful:', ':cry:', ':scream:', ':sob:',
                       ':angry:', ':rage:', ':broken_heart:', ':person_facepalming:', ':thumbsdown:', ':thumbs_down:'
                       ':anguished:', ':weary:', ':cold_sweat:', ':crying_cat_face:', ':rage3:',
                       ':unamused:', ':scream:', ':anger:', ':rage4:', ':disappointed:', ':cry:', ':-1:', ':worried:',
                       ':confused:', ':confounded:', ':sob:', ':tired_face:', ':thumbsdown:', ':fearful:',
                       ':frowning:', ':hushed:', ':disappointed_relieved:', ':fire:', ':flushed_face:', ':white_heart:',
                       ':face_with_symbols_on_mouth:', ':face_screaming_in_fear:', ':angry_face:', ':police_car_light:',
                       ':face_with_raised_eyebrow:', ':crying_face:', ':pouting_face:', ':loudly_crying_face:',
                       ':face_with_raised_eyebrow:', ':nauseated_face:', ':person_shrugging:', ':folded_hands:',
                       ':grimacing_face:', ':lying_face:', ':microbe:', ':hot_face:', ':nauseated_face:', ':black_flag:',
                       ':face_with_medical_mask:', ':face_vomiting:', ':anxious_face_with_sweat:', ':middle_finger:',
                       ':face_with_head-bandage:', ':ogre:', ':radioactive:', ':person_shrugging:', ':circus_tent:',
                       ':fire_engine:', ':police_car:', ':prohibited:', ':stop_sign:', ':sweat_droplets:',
                       ':disappointed_face:', ':zombie:', ':frog_face:', ':mouse:', ':pile_of_poo:',
                       ':slightly_frowning_face:', ':tornado:', ':skull:', ':pouting_cat_face:', ':warning:',
                       ':grinning_face_with_sweat:', ':confetti_ball:', ':unamused_face:',
                       ]


    if token in positive_emojis:
        token = 'EPOS'
    elif token in negative_emojis:
        token = 'ENEG'

    return token


def preprocess_text_before_demojize(text):
    try:
        text = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*',
                      '', text)  # Remove url

        text = re.sub(r'(RT|retweet|from|via)((?:\b\W*@\w+)+)', '', text)  # remove @handle with usermention

        text = re.sub(r'@([A-Za-z0-9_]+)', '', text)  # Remove usermention

        text = re.sub(r'(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)', r' \1 ', text)  # Replaces #hashtag with hashtag

        text = re.sub(r'(-|\[|]|\'|\"|&|,|_|\||:|\.|;)', '', text)  # Remove punctuation and other signs

        text = text.lower()  # Lower letters word

        text = re.sub(r'(.)\1+', r'\1\1', text)  # Convert more than 2 letter repetitions to 2 letter

        text = get_lemmatized_text(text)

        text = remove_unnecessary_pos(text)

    except TypeError:
        text = 'ERROR'

    return text
