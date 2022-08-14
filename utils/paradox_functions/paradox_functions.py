from pydantic import validate_arguments
import pandas as pd
import numpy as np


@validate_arguments()
def data_generation(
        number_of_people_in_room: int,
        sample_size: int
) -> pd.DataFrame:
    """
    Purpose of this function is to generate random matrix from UNIFORM distribution.

    number_of_people_in_room --> will determine number of rows
    sample_size --> will determine number of columns

    :param number_of_people_in_room:
    :type int:
    :param sample_size:
    :type int:
    :return:
    :rtype:
    """

    np_array = np.random.randint(
        low=1,
        high=365,
        size=[number_of_people_in_room, sample_size]
    )
    return pd.DataFrame(
        data=np_array
    )


@validate_arguments(config={'arbitrary_types_allowed': True})
def does_match_happen(s: pd.Series) -> int:
    """
    Purpose of this function is to determine if birthday match between people happend or not.
    If we have two or more people with same birthday, return 1. Otherwise, return 0.

    :param s: List with birthdays.
    :type pd.Series:
    :return: 0 or 1 depending if
    :rtype: int
    """
    if s.value_counts().sum() > s.value_counts().size:
        return 1
    else:
        return 0


@validate_arguments(config={'arbitrary_types_allowed': True})
def create_binary_representation_of_sample_data(df: pd.DataFrame) -> pd.Series:
    """
    Purpose of this function is to transform random DataFrame created in previous step.
    Size of transformed DataFrame would be equal to number of samples i.e. row dimension will be reduced.

    Each column represent one generated sample. E.g. 20 samples -> 20 columns.
    Row represent one element of sample. If sample size is 5 -> 5 rows exist.

    :param df:
    :type df: pd.DataFrame
    :return:
    :rtype: pd.Series
    """
    return df.apply(does_match_happen, axis=0)


@validate_arguments(config={'arbitrary_types_allowed': True})
def create_probability(s: pd.Series) -> float:
    """
    Purpose of this function is to create probability based on relative frequency.

    count(outcome_that_we_like) / count(all_possible_outcomes) * 100

    :param s:
    :type s: pd.Series
    :return:
    :rtype: float
    """
    return s.sum() / s.size


if __name__ == '__main__':

    # Generate random data
    df = data_generation(number_of_people_in_room=23, sample_size=20)

    # Calculate probability
    probability = (
        df.pipe(func=create_binary_representation_of_sample_data)
            .pipe(func=create_probability)
    )

    print(probability)


