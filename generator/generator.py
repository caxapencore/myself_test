from data.data import Person

from faker import Faker

faker_uk = Faker('uk_UA')
Faker.seed()


def generated_person():
    yield Person(
        user_name=faker_uk.first_name() + " ",
        user_surname=faker_uk.last_name() + " ",
        phone_number=faker_uk.phone_number(),
        email=faker_uk.email(),
        password=faker_uk.password(),
    )