import csv


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill,
                 mainskill_grade):
        self.fn = first_name
        self.ln = last_name
        self.email = email
        self.ts = tech_stack
        self.ms = main_skill
        self.ms_gr = mainskill_grade

    def __repr__(self):
        return f"{self.ln} {self.ms}"

    @property
    def full_name(self):
        return f"{self.fn} {self.ln}"

    @classmethod
    def generate_candidates(cls, file_path):
        with open(file_path) as csvfile:

            reader = csv.reader(csvfile)
            next(reader)
            result = []
            for row in reader:
                result.append(cls(row[0].split()[0],
                                  row[0].split()[1],
                                  row[1],
                                  row[2].split("|"),
                                  row[3],
                                  row[4]))
        return result


def main():
    # cand = Candidate("Alex", "Paranichev", "skladinstrumenta@gmail.com",
    # ["Python", "Js"], "Python", "Middle")
    # print(cand.full_name)
    print(Candidate.generate_candidates("candidates.csv"))
    # for x in Candidate.generate_candidates("candidates.csv"):
    #     print(x.__dict__)


if __name__ == "__main__":
    main()
