import pickle


class FixedQueryChecker:

    def __init__(self, fixed_query: str):
        self.fixed_query = fixed_query

    def __call__(self, input_text: str, *args, **kwargs):
        return self.fixed_query.lower() in input_text.lower()


if __name__ == '__main__':
    checker = FixedQueryChecker(fixed_query='Oveys')
    print(checker("Hi, oveys! How you doin?"))



