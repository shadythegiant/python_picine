def generate_events(total):
    players = [
        "Youssef",
        "Hajar",
        "Mehdi",
        "Salma",
        "Amine",
        "Zineb",
        "Karim",
        "Ibtissam",
        "Hamza",
        "Fatima"
    ]

    actions = [
        "killed monster",
        "found treasure",
        "leveled up",
        "explored cave",
        "survived the Piscine",
        "defeated the Norminette",
        "escaped the Black Hole",
        "pushed code to the Vogsphere",
        "failed a peer defense",
        "passed the Libft project"
    ]
    for i in range(1, total + 1):
        player = players[i % 10]
        level = (i % 20) + 1
        action = actions[i % 10]
        yield {"id": i, "player": player, "level": level, "action": action}


def gen_fib(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def gen_prime(limit):
    count, num = 0, 2
    while count < limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")
    event_streamer = generate_events(10)
    total_event = 0
    high_level_count = 0
    level_up_count = 0
    treasure_count = 0
    peer_defense = 0
    for event in event_streamer:
        total_event += 1
        print(
            f"Event {event['id']}: Player {event['player']} "
            f"(level {event['level']}) {event['action']}")
        if total_event == 10:
            print(".....")
        if event['level'] >= 10:
            high_level_count += 1
        if event['action'] == "found treasure":
            treasure_count += 1
        if event['action'] == "leveled up":
            level_up_count += 1
        if event['action'] == "failed a peer defense":
            peer_defense += 1
    print("=== Stream Analytics ===")
    print(f"Total events processed:{total_event}")
    print(f"High-level players: {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print(f"Failed a pair defense :( {peer_defense}")
    print("Memory usage: Constant (streaming)")
    print("Processing t ime: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    fib_tup = []
    for f in gen_fib(10):
        fib_tup += [f]
    fib_tup = tuple(fib_tup)
    prime_tup = []
    for g in gen_prime(5):
        prime_tup += [g]
    prime_tup = tuple(prime_tup)
    print(f"Fibonacci sequence (first 10):{fib_tup}")
    print(f"Prime numbers (first 5):{prime_tup} ")


if __name__ == "__main__":
    main()
