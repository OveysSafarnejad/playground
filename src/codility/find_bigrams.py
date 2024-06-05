def find_bigrams(input_str: str) -> list[tuple]:
    separated_words = input_str.split(' ')
    bigrams = []
    for item in range(len(separated_words) - 1):
        bigrams.append((separated_words[item], separated_words[item + 1]))

    return bigrams


if __name__ == '__main__':
    print(find_bigrams(
        '''is a crucial parameter for controlling the consumption rate of Kafka consumers. It limits the number of records
        fetched in each poll call, helping to balance throughput and latency, and ensuring that the consumer can handle
        the data efficiently. Adjusting this parameter according to your processing capabilities and workload 
        requirements is essential for optimizing your Kafka-based streaming applications.'''
    ))
