class BasicInspection:
    def get_cost(self):
        return 25


class BasicInspectionAndOilChange:
    def get_cost(self):
        return 25 + 29


class BasicInspectionAndOilChangeAndTireRotation:
    def get_cost(self):
        return 25 + 29 + 10


def main():
    print('Basic Inspection: {}'.format(
        BasicInspection().get_cost())
    )
    print('Basic Inspection and Oil Change: {}'.format(
        BasicInspectionAndOilChange().get_cost())
    )
    print('Basic Inspection and OilChange and Tire Rotation: {}'.format(
        BasicInspectionAndOilChangeAndTireRotation().get_cost())
    )


if __name__ == '__main__':
    main()
