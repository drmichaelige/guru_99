# Created by babao at 2/25/2023
Feature: Test Scenarios for Guru99 Bank

  Scenario: User verify the login
        Given Open Demoguru99 page
        When Input text Userid mngr481755
        And Input text Password tArUmun
        And Click Login
        Then Verify the output