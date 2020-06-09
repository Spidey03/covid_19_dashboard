import pytest
from unittest.mock import create_autospec
import datetime
from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.update_statistics_interactor\
    import UpdateStatistics
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from covid_dashboard.exceptions.exceptions\
    import (InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId)


def test_update_statistics_with_invalid_total_confirmed_detail():
    # Arrange
    mandal_id = 1
    total_confirmed = -1
    total_deaths = 4
    total_recovered = 3
    user = {'is_superuser':True}
    date = datetime.date(year=2020, month=5, day=25)
    storage = create_autospec(MandalStorageInterface)
    storage.is_valid_mandal_id.return_value = None
    storage.is_valid_total_confirmed.side_effect = \
        InvalidDetailsForTotalConfirmed
    storage.is_valid_total_deaths.side_effect = None
    storage.is_valid_total_recovered.return_value = None

    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_details_for_total_confirmed.side_effect = \
        InvalidDetailsForTotalConfirmed
    interactor = UpdateStatistics(storage=storage, presenter=presenter)

    # Act
    with pytest.raises(InvalidDetailsForTotalConfirmed):
        interactor.update_statistics(
            user=user,
            mandal_id=mandal_id, date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths, total_recovered=total_recovered
        )


def test_update_statistics_with_invalid_total_death_detail():
    # Arrange
    mandal_id = 1
    total_confirmed = 10
    total_deaths = -5
    total_recovered = 3
    user = {'is_superuser':True}
    date = datetime.date(year=2020, month=5, day=25)
    storage = create_autospec(MandalStorageInterface)
    storage.is_valid_mandal_id.return_value = None
    storage.is_valid_total_confirmed.return_value = None
    storage.is_valid_total_deaths.side_effect = \
        InvalidDetailsForTotalDeaths
    storage.is_valid_total_recovered.return_value = None
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_details_for_total_deaths.side_effect = \
        InvalidDetailsForTotalDeaths
    interactor = UpdateStatistics(storage=storage, presenter=presenter)

    # Act
    with pytest.raises(InvalidDetailsForTotalDeaths):
        interactor.update_statistics(
            user=user,
            mandal_id=mandal_id, date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths, total_recovered=total_recovered
        )


def test_udpate_statistics_with_invalid_total_recovered_detail():
    # Arrange
    mandal_id = 1
    total_confirmed = 10
    total_deaths = 4
    total_recovered = -3
    user = {'is_superuser':True}
    date = datetime.date(year=2020, month=5, day=25)
    storage = create_autospec(MandalStorageInterface)
    storage.is_valid_mandal_id.return_value = None
    storage.is_valid_total_confirmed.return_value = None
    storage.is_valid_total_deaths.return_value = None
    storage.is_valid_total_recovered.side_effect = \
        InvalidDetailsForTotalRecovered
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_details_for_total_recovered.side_effect = \
        InvalidDetailsForTotalRecovered
    interactor = UpdateStatistics(storage=storage, presenter=presenter)

    # Act
    with pytest.raises(InvalidDetailsForTotalRecovered):
        interactor.update_statistics(
            user=user,
            mandal_id=mandal_id, date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths, total_recovered=total_recovered
        )


def test_update_statistics_with_invalid_mandal_id():
    # Arrange
    mandal_id = 10
    total_confirmed = 10
    total_deaths = 4
    total_recovered = 3
    user = {'is_superuser':True}
    date = datetime.date(year=2020, month=5, day=25)
    storage = create_autospec(MandalStorageInterface)
    storage.is_valid_mandal_id.side_effect = InvalidMandalId
    storage.is_valid_total_confirmed.return_value = None
    storage.is_valid_total_deaths.return_value = None
    storage.is_valid_total_recovered.return_value = None
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_details_for_mandal_id.side_effect = \
        InvalidMandalId
    interactor = UpdateStatistics(storage=storage, presenter=presenter)
    date = datetime.date(year=2020, month=5, day=25)
    # Act
    with pytest.raises(InvalidMandalId):
        interactor.update_statistics(
            user=user,
            mandal_id=mandal_id, date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths, total_recovered=total_recovered
        )


def test_update_statistics_with_valid_details():
    # Arrange
    mandal_id = 10
    total_confirmed = 10
    total_deaths = 4
    total_recovered = 3
    user = {'is_superuser':True}
    date = datetime.date(year=2020, month=5, day=25)
    storage = create_autospec(MandalStorageInterface)

    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_details_for_mandal_id.side_effect = \
        InvalidMandalId
    interactor = UpdateStatistics(storage=storage, presenter=presenter)
    date = datetime.date(year=2020, month=5, day=25)
    # Act
    interactor.update_statistics(
        user=user,
        mandal_id=mandal_id, date=date, total_confirmed=total_confirmed,
        total_deaths=total_deaths, total_recovered=total_recovered
        )