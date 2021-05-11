# Generate fake data

## Description

Execute a python script as a Docker container. The script will create some fake data with the following pseudo schema:

```python
{
    "job": str,
    "company": str,
    "ssn": str,
    "residence": str,
    "current_location": List[float],
    "blood_group": str,
    "website": List[str],
    "username": str,
    "name": str,
    "sex": str,
    "address": str,
    "mail": str,
    "birthdate": str,
    "dating": {
        "bio": str,
        "has_children": bool,
        "days_since_last_date": int,
        "total_dates_since_joined": int
    }
}
```

## How to

**Step 1**

Clone the repo

**Step 2**

Build the Docker image

```sh
docker build -t faker .
```

**Step 3**

Run the Docker container to generate `--nb_docs xx` documents with seed `--seed x` in a file called `fake_data.json` which will be mounted to your current directory

```sh
docker run -v ${PWD}:/data faker --seed 42 --nb_docs 10
```

## Example

Copy and paste the following command for a quick start

```sh
git clone https://github.com/VildMedPap/generate_fake_data.git
cd generate_fake_data
docker build -t faker .
docker run -v ${PWD}:/data faker --seed 42 --nb_docs 2
```

and you'll get a `fake_data.json` file with the following content

```json
[
    {
        "job": "Clinical research associate",
        "company": "Figueroa and Sons",
        "ssn": "229-18-1680",
        "residence": "600 Jeffery Parkways\nNew Jamesside, IN 59379",
        "current_location": [68.1798025, -30.647502],
        "blood_group": "A+",
        "website": [
            "https://moore-bernard.com/",
            "http://www.davis-abbott.org/"
        ],
        "username": "smiller",
        "name": "Nicholas Herrera",
        "sex": "M",
        "address": "310 Kendra Common Apt. 164\nReidstad, MN 47067",
        "mail": "elizabethmiles@hotmail.com",
        "birthdate": "1993-07-22T00:00:00.000+00:00",
        "dating": {
            "bio": "Move each left establish. Detail food shoulder argue start source husband.",
            "has_children": true,
            "days_since_last_date": 108,
            "total_dates_since_joined": 9
        }
    },
    {
        "job": "International aid/development worker",
        "company": "Rios Group",
        "ssn": "659-59-2341",
        "residence": "884 Hurst Locks\nJeffreyberg, NM 12416",
        "current_location": [-77.352295, -121.13257],
        "blood_group": "B+",
        "website": ["https://www.james-ferrell.net/", "https://www.le.com/"],
        "username": "teresa28",
        "name": "Jeffrey Chavez",
        "sex": "M",
        "address": "PSC 4893, Box 2528\nAPO AP 00575",
        "mail": "tracy15@yahoo.com",
        "birthdate": "1937-12-12T00:00:00.000+00:00",
        "dating": {
            "bio": "Water beat magazine attorney set she campaign.",
            "has_children": false,
            "days_since_last_date": 484,
            "total_dates_since_joined": 8
        }
    }
]
```
