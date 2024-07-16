from nada_dsl import *

def nada_main():
    # Define the party
    party = Party(name="Party1")

    # Define the inputs for the party
    input1 = Input(name="input1", party=party)
    input2 = Input(name="input2", party=party)

    # Define secret integers based on the inputs
    secret_int1 = SecretInteger(input1)
    secret_int2 = SecretInteger(input2)

    # Perform secure addition
    result = secret_int1 + secret_int2

    # Define the output and specify the party that will receive it
    output = Output(result, "secure_sum", party)

    return [output]