# https://www.acmicpc.net/problem/10866
# 덱 (정수를 저장하는 덱)
import sys


class Deck:
    deck = []

    def get_deck(self):
        return self.deck

    def push_front(self, x):
        self.deck.insert(0, x)

    def push_back(self, x):
        self.deck.append(x)

    def pop_front(self):
        return self.deck.pop(0) if self.deck else -1

    def pop_back(self):
        return self.deck.pop() if self.deck else -1

    def size(self):
        return len(self.deck)

    def empty(self):
        return 1 if not self.deck else 0

    def front(self):
        return self.deck[0] if self.deck else -1

    def back(self):
        return self.deck[-1] if self.deck else -1


class CommandResolver:
    @staticmethod
    def resolve(d, cmd):

        commands = cmd.split()
        command = commands[0]
        # print("d:", d.get_deck(), end=" -> ")
        # print("commands:", commands)

        if command == 'push_front':
            d.push_front(commands[1])
        elif command == 'push_back':
            d.push_back(commands[1])
        elif command == 'pop_front':
            print(d.pop_front())
        elif command == 'pop_back':
            print(d.pop_back())
        elif command == 'size':
            print(d.size())
        elif command == 'empty':
            print(d.empty())
        elif command == 'front':
            print(d.front())
        elif command == 'back':
            print(d.back())
        else:
            return None


N = int(input())
deck = Deck()

for _ in range(N):
    line = sys.stdin.readline()
    CommandResolver.resolve(deck, line)
