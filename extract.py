"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        lst_neos = list()
        for line in reader:
            line["name"] = line["name"] or None
            line["diameter"] = float(line["diameter"]) if line["diameter"] else None
            if line["pha"] in ["", "N"]:
                line["pha"] = False
            else:
                line["pha"] = True
            neo = NearEarthObject(designation = line["pdes"], name = line["name"], diameter = line["diameter"], hazardous = line["pha"])
            lst_neos.append(neo)
    return lst_neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, "r") as json_file:
        reader = json.load(json_file)
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        lst_approaches = list()
        for line in reader:
            approach = CloseApproach(designation = line["des"], time = line["cd"], distance = float(line["dist"]), velocity = float(line["v_rel"])) 
            lst_approaches.append(approach)
    return lst_approaches
