class Flowers:
    def __init__(self, name_flower, freshness_day, lifetime_day, color, stem_length, cost):
        self.name_flower = name_flower
        self.freshness_day = freshness_day  # сколько дней уже стоит
        self.lifetime_day = lifetime_day  # средняя продолжительность жизни в днях
        self.color = color
        self.stem_length = stem_length
        self.cost = cost

    def __str__(self):
        return f'{self.name_flower}'

    def __repr__(self):
        return f'{self.name_flower}'


class Roses(Flowers):
    type_flower = 'розы'


class Pions(Flowers):
    type_flower = 'пионы'


class Lilies(Flowers):
    type_flower = 'лилии'


class Chrysanthemums(Flowers):
    type_flower = 'хризантемы'


class Asters(Flowers):
    type_flower = 'астры'


class Irises(Flowers):
    type_flower = 'ирисы'


class Gladiolus(Flowers):
    type_flower = 'гладиолусы'


class Narcissus(Flowers):
    type_flower = 'нарциссы'


red_rose = Roses('Красная роза', 3, 7, 'красный', 60, 300)
white_rose = Roses('Белая роза', 4, 8, 'белый', 65, 350)

red_pion = Pions('Красный пион', 2, 5, 'красный', 50, 400)
white_pion = Pions('Белый пион', 3, 6, 'белый', 55, 450)

red_lily = Lilies('Красная лилия', 4, 9, 'красный', 70, 500)
white_lily = Lilies('Белая лилия', 5, 10, 'белый', 75, 550)

red_chrysanthemum = Chrysanthemums('Красная хризантема', 5, 12, 'красный', 50, 200)
white_chrysanthemum = Chrysanthemums('Белая хризантема', 6, 14, 'белый', 55, 250)

red_aster = Asters('Красная астра', 3, 6, 'красный', 40, 150)
white_aster = Asters('Белая астра', 4, 7, 'белый', 45, 180)

red_iris = Irises('Красный ирис', 2, 5, 'красный', 60, 280)
white_iris = Irises('Белый ирис', 3, 6, 'белый', 65, 320)

red_gladiolus = Gladiolus('Красный гладиолус', 5, 10, 'красный', 80, 350)
white_gladiolus = Gladiolus('Белый гладиолус', 6, 12, 'белый', 85, 400)

red_narcissus = Narcissus('Красный нарцисс', 2, 4, 'красный', 30, 120)
white_narcissus = Narcissus('Белый нарцисс', 3, 5, 'белый', 35, 150)


class Bouquet:

    def __init__(self, flowers_list):
        self.flowers_list = flowers_list

    def search_flowers_lifetime(self, lifetime_day_search):
        search_list = [flower.name_flower for flower in self.flowers_list if flower.lifetime_day == lifetime_day_search]
        # способ через цикл (оставляю для себя в будущем, когда буду возвращаться к этой теме, чтоб понять)
        # search_list = []
        # for flower in self.flowers_list:
        #     if flower.lifetime_day == lifetime_day_search:
        #         search_list.append(flower.name_flower)
        return search_list

    def total_cost(self):
        result = 0
        for flower in self.flowers_list:
            result += flower.cost
        return result

    def avg_lifetime_day(self):
        sum_day = 0
        for flower in self.flowers_list:
            sum_day += flower.lifetime_day
        return sum_day / len(self.flowers_list)

    def sort_cost(self):
        return sorted(self.flowers_list, key=lambda flower: flower.cost)

    def sort_fresh(self):
        return sorted(self.flowers_list, key=lambda flower: flower.freshness_day)

    def sort_stem_length(self):
        return sorted(self.flowers_list, key=lambda flower: flower.stem_length)

    def sort_color(self):
        return sorted(self.flowers_list, key=lambda flower: flower.color)


red_bouquet = Bouquet([
    red_rose, red_rose, red_rose,
    red_pion, red_pion,
    red_lily,
    red_chrysanthemum, red_chrysanthemum,
    red_aster, red_aster,
    red_iris, red_iris,
    red_gladiolus,
    red_narcissus, red_narcissus
])

white_bouquet = Bouquet([
    white_rose, white_rose,
    white_lily, white_lily,
    white_chrysanthemum,
    white_aster, white_aster, white_aster,
    white_iris,
    white_gladiolus, white_gladiolus,
    white_narcissus, white_narcissus
])

mixed_bouquet = Bouquet([
    red_rose, white_rose,
    red_pion, white_pion,
    red_lily, white_lily,
    red_chrysanthemum, white_chrysanthemum,
    red_aster, white_aster,
    red_iris, white_iris,
    red_gladiolus, white_gladiolus,
    red_narcissus, white_narcissus
])

print(red_bouquet.total_cost())
print(red_bouquet.search_flowers_lifetime(5))
print(red_bouquet.avg_lifetime_day())
print(red_bouquet.sort_cost())
print(red_bouquet.sort_fresh())
print(mixed_bouquet.sort_color())
