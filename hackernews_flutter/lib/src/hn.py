import re
from datetime import datetime

nws = [
    {
        "created_at": "2019-05-07T20:40:04.000Z",
        "title": "Flutter: a Portable UI Framework for Mobile, Web, Embedded, and Desktop",
        "url": "https://developers.googleblog.com/2019/05/Flutter-io19.html",
        "author": "mikece",
        "points": 654,
        "story_text": None,
        "comment_text": None,
        "num_comments": 449,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1557261604,
        "relevancy_score": 8818,
        "_tags": ["story", "author_mikece", "story_19853247"],
        "objectID": "19853247",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e: a Portable UI Framework for Mobile, Web, Embedded, and Desktop",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://developers.googleblog.com/2019/05/\u003cem\u003eFlutter\u003c/em\u003e-io19.html",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "mikece",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2018-12-04T17:34:43.000Z",
        "title": "Google's cross-platform Flutter UI toolkit goes 1.0",
        "url": "https://techcrunch.com/2018/12/04/googles-cross-platform-flutter-ui-toolkit-hits-version-1-0/",
        "author": "mikece",
        "points": 545,
        "story_text": None,
        "comment_text": None,
        "num_comments": 327,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1543944883,
        "relevancy_score": 8522,
        "_tags": ["story", "author_mikece", "story_18601588"],
        "objectID": "18601588",
        "_highlightResult": {
            "title": {
                "value": "Google's cross-platform \u003cem\u003eFlutter\u003c/em\u003e UI toolkit goes 1.0",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://techcrunch.com/2018/12/04/googles-cross-platform-\u003cem\u003eflutter\u003c/em\u003e-ui-toolkit-hits-version-1-0/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "mikece",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2015-11-06T05:55:37.000Z",
        "title": "Flutter – Cross-platform mobile framework from Google",
        "url": "http://flutter.io/faq/",
        "author": "_r5wf",
        "points": 455,
        "story_text": None,
        "comment_text": None,
        "num_comments": 275,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1446789337,
        "relevancy_score": 6358,
        "_tags": ["story", "author__r5wf", "story_10518033"],
        "objectID": "10518033",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e – Cross-platform mobile framework from Google",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "http://\u003cem\u003eflutter\u003c/em\u003e.io/faq/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {"value": "_r5wf", "matchLevel": "none", "matchedWords": []}
        }
    },
    {
        "created_at": "2018-02-27T15:42:44.000Z",
        "title": "Announcing Flutter beta 1: Build beautiful native apps",
        "url": "https://developers.googleblog.com/2018/02/announcing-flutter-beta-1.html",
        "author": "nicpottier",
        "points": 373,
        "story_text": None,
        "comment_text": None,
        "num_comments": 338,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1519746164,
        "relevancy_score": 7984,
        "_tags": ["story", "author_nicpottier", "story_16474327"],
        "objectID": "16474327",
        "_highlightResult": {
            "title": {
                "value": "Announcing \u003cem\u003eFlutter\u003c/em\u003e beta 1: Build beautiful native apps",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://developers.googleblog.com/2018/02/announcing-\u003cem\u003eflutter\u003c/em\u003e-beta-1.html",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "nicpottier",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2019-04-25T13:21:02.000Z",
        "title": "Flutter desktop shells",
        "url": "https://github.com/flutter/flutter/wiki/Desktop-shells",
        "author": "Memosyne",
        "points": 370,
        "story_text": None,
        "comment_text": None,
        "num_comments": 315,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1556198462,
        "relevancy_score": 8791,
        "_tags": ["story", "author_Memosyne", "story_19747750"],
        "objectID": "19747750",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e desktop shells",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://github.com/\u003cem\u003eflutter\u003c/em\u003e/\u003cem\u003eflutter\u003c/em\u003e/wiki/Desktop-shells",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "Memosyne",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2020-01-03T21:26:48.000Z",
        "title": "Flutter vs. Other Mobile Development Frameworks: A UI and Performance Experiment",
        "url": "https://blog.codemagic.io/flutter-vs-ios-android-reactnative-xamarin/",
        "author": "Rubytron",
        "points": 370,
        "story_text": None,
        "comment_text": None,
        "num_comments": 178,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1578086808,
        "_tags": ["story", "author_Rubytron", "story_21950558"],
        "objectID": "21950558",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e vs. Other Mobile Development Frameworks: A UI and Performance Experiment",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://blog.codemagic.io/\u003cem\u003eflutter\u003c/em\u003e-vs-ios-android-reactnative-xamarin/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "Rubytron",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2013-08-27T18:28:32.000Z",
        "title": "Flutter: $20 Wireless Arduino with 1 km range",
        "url": "http://www.kickstarter.com/projects/2021474419/flutter-20-wireless-arduino-with-half-mile-1km-ran",
        "author": "trafnar",
        "points": 347,
        "story_text": "",
        "comment_text": None,
        "num_comments": 139,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1377628112,
        "relevancy_score": 4826,
        "_tags": ["story", "author_trafnar", "story_6285231"],
        "objectID": "6285231",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e: $20 Wireless Arduino with 1 km range",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "http://www.kickstarter.com/projects/2021474419/\u003cem\u003eflutter\u003c/em\u003e-20-wireless-arduino-with-half-mile-1km-ran",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "trafnar",
                "matchLevel": "none",
                "matchedWords": []
            },
            "story_text": {"value": "", "matchLevel": "none", "matchedWords": []}
        }
    },
    {
        "created_at": "2018-11-23T11:19:01.000Z",
        "title": "Flutter: the good, the bad and the ugly",
        "url": "https://medium.com/asos-techblog/flutter-vs-react-native-for-ios-android-app-development-c41b4e038db9",
        "author": "marcobellinaso",
        "points": 307,
        "story_text": None,
        "comment_text": None,
        "num_comments": 217,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1542971941,
        "relevancy_score": 8494,
        "_tags": ["story", "author_marcobellinaso", "story_18515789"],
        "objectID": "18515789",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e: the good, the bad and the ugly",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://medium.com/asos-techblog/\u003cem\u003eflutter\u003c/em\u003e-vs-react-native-for-ios-android-app-development-c41b4e038db9",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "marcobellinaso",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2017-08-19T13:26:09.000Z",
        "title": "Flutter – A mobile app SDK for iOS and Android",
        "url": "https://flutter.io/",
        "author": "Mayzie",
        "points": 277,
        "story_text": None,
        "comment_text": None,
        "num_comments": 97,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1503149169,
        "relevancy_score": 7607,
        "_tags": ["story", "author_Mayzie", "story_15053218"],
        "objectID": "15053218",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e – A mobile app SDK for iOS and Android",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://\u003cem\u003eflutter\u003c/em\u003e.io/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "Mayzie",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2020-02-29T23:57:52.000Z",
        "title": "Flutter and Dart, or how to quickly build a mobile app without losing your hair",
        "url": "https://altkomsoftware.pl/blog/flutter-dart-quickly-build-mobile-app-without-losing-much-hair/",
        "author": "witek1902",
        "points": 252,
        "story_text": None,
        "comment_text": None,
        "num_comments": 174,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1583020672,
        "_tags": ["story", "author_witek1902", "story_22454115"],
        "objectID": "22454115",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e and Dart, or how to quickly build a mobile app without losing your hair",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://altkomsoftware.pl/blog/\u003cem\u003eflutter\u003c/em\u003e-dart-quickly-build-mobile-app-without-losing-much-hair/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "witek1902",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2017-06-23T06:40:20.000Z",
        "title": "Google’s Flutter = React and Java Swing",
        "url": "https://codeburst.io/googles-flutter-react-java-swing-8174c8d9d402",
        "author": "kiyanwang",
        "points": 249,
        "story_text": None,
        "comment_text": None,
        "num_comments": 152,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1498200020,
        "relevancy_score": 7500,
        "_tags": ["story", "author_kiyanwang", "story_14617392"],
        "objectID": "14617392",
        "_highlightResult": {
            "title": {
                "value": "Google’s \u003cem\u003eFlutter\u003c/em\u003e = React and Java Swing",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://codeburst.io/googles-\u003cem\u003eflutter\u003c/em\u003e-react-java-swing-8174c8d9d402",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "kiyanwang",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2012-03-11T23:20:04.000Z",
        "title": "Show HN: Flutter - Control Spotify or iTunes Using Gestures thru Webcam",
        "url": "http://flutter.io",
        "author": "mehuln",
        "points": 234,
        "story_text": "",
        "comment_text": None,
        "num_comments": 126,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1331508004,
        "relevancy_score": 3790,
        "_tags": ["story", "author_mehuln", "story_3691588", "show_hn"],
        "objectID": "3691588",
        "_highlightResult": {
            "title": {
                "value": "Show HN: \u003cem\u003eFlutter\u003c/em\u003e - Control Spotify or iTunes Using Gestures thru Webcam",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "http://\u003cem\u003eflutter\u003c/em\u003e.io",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "mehuln",
                "matchLevel": "none",
                "matchedWords": []
            },
            "story_text": {"value": "", "matchLevel": "none", "matchedWords": []}
        }
    },
    {
        "created_at": "2019-08-05T05:35:09.000Z",
        "title": "Flutter looks good, but is painful",
        "url": "https://medium.com/@bernaferrari/from-android-dev-flutter-looks-good-but-is-painful-here-are-my-frustrations-with-it-81b4bbe739f8",
        "author": "xhroot",
        "points": 208,
        "story_text": None,
        "comment_text": None,
        "num_comments": 187,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1564983309,
        "relevancy_score": 8991,
        "_tags": ["story", "author_xhroot", "story_20611544"],
        "objectID": "20611544",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e looks good, but is painful",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://medium.com/@bernaferrari/from-android-dev-\u003cem\u003eflutter\u003c/em\u003e-looks-good-but-is-painful-here-are-my-frustrations-with-it-81b4bbe739f8",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "xhroot",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2020-03-18T11:44:18.000Z",
        "title": "Show HN: Helm - A Flutter app that gamifies stress/anxiety/depression management",
        "url": "https://github.com/chuabingquan/helm",
        "author": "chipneverdies",
        "points": 196,
        "story_text": None,
        "comment_text": None,
        "num_comments": 61,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1584531858,
        "_tags": ["story", "author_chipneverdies", "story_22615515", "show_hn"],
        "objectID": "22615515",
        "_highlightResult": {
            "title": {
                "value": "Show HN: Helm - A \u003cem\u003eFlutter\u003c/em\u003e app that gamifies stress/anxiety/depression management",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://github.com/chuabingquan/helm",
                "matchLevel": "none",
                "matchedWords": []
            },
            "author": {
                "value": "chipneverdies",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2019-01-21T08:35:41.000Z",
        "title": "Flutter: Futures, Isolates, Event Loop",
        "url": "https://www.didierboelens.com/2019/01/futures---isolates---event-loop/",
        "author": "yannikyeo",
        "points": 193,
        "story_text": None,
        "comment_text": None,
        "num_comments": 39,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1548059741,
        "relevancy_score": 8615,
        "_tags": ["story", "author_yannikyeo", "story_18958747"],
        "objectID": "18958747",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e: Futures, Isolates, Event Loop",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://www.didierboelens.com/2019/01/futures---isolates---event-loop/",
                "matchLevel": "none",
                "matchedWords": []
            },
            "author": {
                "value": "yannikyeo",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2018-06-20T15:28:17.000Z",
        "title": "Announcing Flutter Release Preview 1",
        "url": "https://medium.com/flutter-io/flutter-release-preview-1-943a9b6ee65a",
        "author": "mattsolle",
        "points": 180,
        "story_text": None,
        "comment_text": None,
        "num_comments": 82,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1529508497,
        "relevancy_score": 8198,
        "_tags": ["story", "author_mattsolle", "story_17356280"],
        "objectID": "17356280",
        "_highlightResult": {
            "title": {
                "value": "Announcing \u003cem\u003eFlutter\u003c/em\u003e Release Preview 1",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://medium.com/\u003cem\u003eflutter\u003c/em\u003e-io/\u003cem\u003eflutter\u003c/em\u003e-release-preview-1-943a9b6ee65a",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "mattsolle",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2017-05-28T02:23:02.000Z",
        "title": "Exploring Flutter for Cross-Platform Mobile Development",
        "url": "https://sethlopez.me/article/exploring-flutter-for-cross-platform-mobile-development/",
        "author": "amarokaz",
        "points": 166,
        "story_text": None,
        "comment_text": None,
        "num_comments": 87,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1495938182,
        "relevancy_score": 7446,
        "_tags": ["story", "author_amarokaz", "story_14432857"],
        "objectID": "14432857",
        "_highlightResult": {
            "title": {
                "value": "Exploring \u003cem\u003eFlutter\u003c/em\u003e for Cross-Platform Mobile Development",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://sethlopez.me/article/exploring-\u003cem\u003eflutter\u003c/em\u003e-for-cross-platform-mobile-development/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "amarokaz",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    },
    {
        "created_at": "2018-06-03T02:55:36.000Z",
        "title": "Ready for Production Apps: Flutter Beta 3",
        "url": "https://developers.googleblog.com/2018/05/ready-for-production-apps-flutter-beta-3.html",
        "author": "grigy",
        "points": 160,
        "story_text": None,
        "comment_text": None,
        "num_comments": 104,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1527994536,
        "relevancy_score": 8158,
        "_tags": ["story", "author_grigy", "story_17217673"],
        "objectID": "17217673",
        "_highlightResult": {
            "title": {
                "value": "Ready for Production Apps: \u003cem\u003eFlutter\u003c/em\u003e Beta 3",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://developers.googleblog.com/2018/05/ready-for-production-apps-\u003cem\u003eflutter\u003c/em\u003e-beta-3.html",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {"value": "grigy", "matchLevel": "none", "matchedWords": []}
        }
    },
    {
        "created_at": "2013-10-02T22:20:51.000Z",
        "title": "Flutter (YC W12) acquired by Google",
        "url": "https://flutterapp.com/",
        "author": "DesaiAshu",
        "points": 157,
        "story_text": "",
        "comment_text": None,
        "num_comments": 24,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1380752451,
        "relevancy_score": 4892,
        "_tags": ["story", "author_DesaiAshu", "story_6485824"],
        "objectID": "6485824",
        "_highlightResult": {
            "title": {
                "value": "\u003cem\u003eFlutter\u003c/em\u003e (YC W12) acquired by Google",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://\u003cem\u003eflutter\u003c/em\u003eapp.com/",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "DesaiAshu",
                "matchLevel": "none",
                "matchedWords": []
            },
            "story_text": {"value": "", "matchLevel": "none", "matchedWords": []}
        }
    },
    {
        "created_at": "2018-06-16T18:16:04.000Z",
        "title": "What It Was Like to Write a Full-Blown Flutter App",
        "url": "https://medium.com/@seenickcode/what-it-was-like-to-write-a-full-blown-flutter-app-330d8202825b",
        "author": "timsneath",
        "points": 153,
        "story_text": None,
        "comment_text": None,
        "num_comments": 57,
        "story_id": None,
        "story_title": None,
        "story_url": None,
        "parent_id": None,
        "created_at_i": 1529172964,
        "relevancy_score": 8185,
        "_tags": ["story", "author_timsneath", "story_17328603"],
        "objectID": "17328603",
        "_highlightResult": {
            "title": {
                "value": "What It Was Like to Write a Full-Blown \u003cem\u003eFlutter\u003c/em\u003e App",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "url": {
                "value": "https://medium.com/@seenickcode/what-it-was-like-to-write-a-full-blown-\u003cem\u003eflutter\u003c/em\u003e-app-330d8202825b",
                "matchLevel": "full",
                "fullyHighlighted": False,
                "matchedWords": ["flutter"]
            },
            "author": {
                "value": "timsneath",
                "matchLevel": "none",
                "matchedWords": []
            }
        }
    }
]

for news in nws:
    date_match = re.match('([0-9\-]+)[T]([0-9:]+)', news["created_at"])
    created_at = " ".join(date_match.groups())
    created_date = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    ago_time = datetime.now() - created_date
    ago = None
    if(ago_time.days < 365):
        ago = str(ago_time.days) + ' days'
    else:
        ago = str(round(ago_time.days / 365)) + ' years'

    print('''Article(text: "{}",
              domain: "{}",
              by: "{}",
              age: "{}",
              score: {},
              commentsScore: {}),'''.format(news["title"], news["url"], news["author"], ago, news["points"], news["num_comments"]))
