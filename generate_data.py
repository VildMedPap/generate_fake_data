import argparse

import simplejson as json
from faker import Faker

faker = Faker()

# Create the parser
my_parser = argparse.ArgumentParser(description='Generate fake data')

# Add the arguments
my_parser.add_argument('-s', '--seed', type=int, help='Set seed for randomization')
my_parser.add_argument('-n', '--nb_docs', type=int, help='Number of documents to generate')

# Execute the parse_args() method
args = my_parser.parse_args()

seed = args.seed
nb_docs = args.nb_docs

if seed is not None:
    Faker.seed(seed)

if nb_docs is None:
    nb_docs = 10

data = []
for _ in range(nb_docs):
    profile = faker.profile()
    dating = {
        "bio": faker.paragraph(nb_sentences=faker.random_int(1, 15)),
        "has_children": faker.boolean(),
        "days_since_last_date": faker.random_int(0, 500),
        "total_dates_since_joined": faker.random_digit(),
    }
    profile["dating"] = dating
    profile["birthdate"] = profile["birthdate"].isoformat() + "T00:00:00.000+00:00"
    data.append(profile)

with open('/data/fake_data.json', 'w') as fp:
    json.dump(data, fp)
