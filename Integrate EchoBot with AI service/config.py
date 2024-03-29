#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    #Added to support interaction with Azure AI Language API
    ENDPOINT_URI = os.environ.get("MicrosoftAIServiceEndpoint","https://t6languageservice1.cognitiveservices.azure.com/")
    print(f"ENDPOINT_URI={ENDPOINT_URI}")
    API_KEY = os.environ.get("MicrosoftAPIKey","00faabab8cb34796bf412d7de07ae676")

