def load_files(files):
    pairset_list = [read_pairfile(f) for f in files]
    return Dataset(pairset_list)


def read_pairfile(file):
    with open(file, mode="r") as f:
        source_name = ""
        pairs = []
        for line in f.readlines():
            # Remove comments
            if line[0] == "#":
                continue

            if line[0] == "[":
                source_name = line.replace("[", "").replace("]", "").replace("\n", "")
                continue
            else:
                pairs = pairs + [
                    (source_name, target_name) for target_name in line.split()
                ]
        return pairs


class Dataset:
    def __init__(self, pairset_list):
        self.pairset_list = pairset_list
        self.intersection = None

    def get_sets(self):
        return self.pairset_list

    def create_intersection(self):
        intersection = self.intersection
        for s in [set(l) for l in self.pairset_list]:
            if intersection is None:
                intersection = s
            else:
                intersection = intersection & s
        self.intersection = intersection

    def to_dat(self, output_filepath):
        pair_list = list(self.intersection)
        obj = {}
        for pair in sorted(pair_list):
            source = pair[0]
            target = pair[1]
            if source not in obj.keys():
                obj[source] = [target]
            else:
                obj[source].append(target)

        result = ""
        for source, target_list in obj.items():
            result += f"[{source}]\n"
            result += " ".join(sorted(target_list)) + "\n"

        with open(output_filepath, mode="w") as f:
            f.write(result)
