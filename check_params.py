import sys

limit = 1010


def verify(params):
    li = ["output", "start", "end", "forms"]
    for s in li:
        if s not in params:
            msg = "Variable {} is missing or misnamed in parameters.".format(s)
            sys.exit(msg)


def validate(output_file, start, end, forms):
    if not output_file.endswith(".txt"):
        msg = output_file + " is not a valid filename to write to. " \
                            "It must end in '.txt'."
        sys.exit(msg)

    if start < 1 or start >= limit:
        msg = "{} is not a valid value for 'start'. " \
              "It must be at least 1 and at most 1 less than {}." \
            .format(str(start), str(limit))
        sys.exit(msg)

    if end < start or end > limit:
        msg = "{} is not a valid value for 'end'. " \
              "It must be at least 1 more than 'start' and at most {}." \
            .format(str(end), str(limit))
        sys.exit(msg)

    check_forms(forms)


def check_forms(forms):
    li = ["all", "none", "forms", "aesthetic only", "gender-based",
          "regional variant", "mega evolution", "primal", "gigantamax",
          "unique", "totem", "partner", "cosplay pikachu", "pikachu in a cap",
          "ash greninja", "disguise", "eternamax", "mounts"]
    for s in li:
        if s not in forms:
            msg = "Variable '{}' is missing or misnamed in forms.".format(s)
            sys.exit(msg)
        if not isinstance(forms[s], bool):
            msg = "Variable '{}' must be either 'true' or 'false'.".format(s)
            sys.exit(msg)
