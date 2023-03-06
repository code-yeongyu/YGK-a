# YGKA 🤖

[![codecov](https://codecov.io/gh/code-yeongyu/YGK-a/branch/master/graph/badge.svg?token=GB79Y7PEHU)](https://codecov.io/gh/code-yeongyu/YGK-a)
[![Release Package to PyPI](https://github.com/code-yeongyu/YGK-a/actions/workflows/release.yml/badge.svg)](https://github.com/code-yeongyu/YGK-a/actions/workflows/release.yml)
[![PyPI version](https://badge.fury.io/py/ygka.svg)](https://badge.fury.io/py/ygka)

YGKA is an advanced ChatGPT client for shell that acts as Your Genius Knowledgeable Assistant. YGKA supports Unix/Linux pipelines and requires no setting up of tokens or API keys. Furthermore, if you want to use an OpenAI API key, you can easily configure it.

![demo](https://raw.githubusercontent.com/code-yeongyu/YGK-a/master/images/factorial.png)

## Key Features 💡

- Supports Unix/Linux pipelines
- Ready to use without setting up tokens or API keys

## Prerequisites 📚

- Python 3.9+
- ChatGPT Account (or OpenAI Account)

## Getting Started 🚀

To begin using YGKA, install it with pip:

```sh
pip install ygka
```

Once you've installed YGKA, you can start using it right away, like following.

![demo](https://raw.githubusercontent.com/code-yeongyu/YGK-a/master/images/first.png)

To execute a command, use the following syntax:

```sh
ygka "<your command here>"
```

For example, to ask "hello?" using YGKA, you can use the following command:

```sh
ygka "hello?"
```

You can also use YGKA with Unix pipeline. For example, to ask "what is this file?" while viewing the contents of a text file, you can use the following command:

```sh
cat textfile.txt | ygka "what is this file?"
```

## Advanced Settings 🛠

By default, `YGKA` is configured to use the reverse-engineered ChatGPT client and retrieve login information from your browser, so you don't need to configure anything to use `YGKA`. However, for those who want to use different models with an OpenAI API Key, you can configure it as follows:

1. Create an account on OpenAI.
1. Go to <https://platform.openai.com/account/api-keys> and copy your API key.
1. Modify or create the `~/.ygka_config.json` file as follows:

```json
{
    ...
    "language_model": <language model of your preference>, //"official_chatgpt"
    "openai_api_key": <your OpenAI API key>
}
```

Here, you can specify the language model of your preference and add your OpenAI API key.

## Inspired By 🎨

- YeonGyu Kim: My name. The project is named after me.
- [AiShell](https://github.com/code-yeongyu/AiShell): A Natural Language Shell Powered by ChatGPT, is a brother project of YGKA that provides a similar functionality.
- [loz](https://github.com/joone/loz): A nodejs version of a GPT3 client that does similar things as YGKA.

## Contributions 💬

Feel free to contribute to YGKA by adding more functionality or fixing bugs.
