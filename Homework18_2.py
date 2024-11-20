from colorama import Fore # pip install colorama
from names_generator import generate_name # pip install names-generator

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker) and worker not in self._workers:
            self._workers.append(worker)
            worker._boss = self
        elif not isinstance(worker, Worker):
            raise ValueError(f"{Fore.RED} Можно добавлять только экземпляры Worker.")

    def remove_worker(self, worker):
        if worker in self._workers:
            self._workers.remove(worker)
            worker._boss = None

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if value is not None and not isinstance(value, Boss):
            raise ValueError(f"{Fore.RED} Boss должен быть экземпляром Boss или None.")
        if self._boss is not None:
            self._boss.remove_worker(self)
        self._boss = value
        if value is not None:
            value.add_worker(self)

boss = Boss(1, generate_name(style='capital'), "TestCo")

worker1 = Worker(101, generate_name(style='capital'), "TestCo", boss)
worker2 = Worker(102, generate_name(style='capital'), "TestCo", boss)

print(f"Работники босса {boss.name} (ID: {boss.id}):")
for worker in boss.workers:
    print(f"  - {worker.name} (ID: {worker.id})")

print ('#######' * 20)

new_boss = Boss(2, generate_name(style='capital'), "TestCo")
worker1.boss = new_boss

print(f"\nРаботники босса  {boss.name} (ID: {boss.id}):")
for worker in boss.workers:
    print(f"  - {worker.name} (ID: {worker.id})")

print(f"\nРаботники босса  {new_boss.name} (ID: {new_boss.id}):")
for worker in new_boss.workers:
    print(f"  - {worker.name} (ID: {worker.id})")
