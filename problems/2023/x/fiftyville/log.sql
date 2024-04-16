-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Read any crime scene reports on July 28th, 2021 at Humphrey Street
SELECT *
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = 'Humphrey Street';

-- Read any interview transcript on July 28th, 2021 that mentioned 'bakery'
SELECT *
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%bakery%';

-- Read the bakery security logs around 10:15am - 10:25am for cars that left the parking lot
SELECT *
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute >= 15
AND minute <= 25
AND activity = 'exit';

-- Read ATM transactions at Leggett Street for a withdraw transaction
SELECT *
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Read phone calls that has a duration of less than 60 seconds
SELECT *
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Read the earliest flight out of Fiftyville
SELECT *
FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY HOUR;

-- Read passengers info for flight 36
SELECT *
FROM passengers
WHERE flight_id = 36;

-- Find out who the thief is by combining all of the previous values
SELECT people.name AS 'The THIEF'
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE people.phone_number IN
    (SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60)
AND people.license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute >= 15
    AND minute <= 25
    AND activity = 'exit')
AND bank_accounts.account_number IN
    (SELECT account_number
    FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw')
AND passport_number IN
    (SELECT passport_number
    FROM passengers
    WHERE flight_id =
        (SELECT id
        FROM flights
        WHERE year = 2021
        AND month = 7
        AND day = 29
        ORDER BY HOUR
        LIMIT 1);
    )

-- Find out what city the thief escaped to by querying flight 36
SELECT city AS 'The city the thief ESCAPED TO'
FROM airports
WHERE id =
    (SELECT destination_airport_id
    FROM flights
    WHERE id =
    (SELECT id
    FROM flights
    WHERE year = 2021
    AND month = 7
    AND day = 29
    ORDER BY HOUR
    LIMIT 1)
    );
    
-- Find out who is the accomplice by querying who the number (367) 555-5533 is calling
SELECT name AS 'The ACCOMPLICE'
FROM people
WHERE phone_number =
    (SELECT receiver
    FROM phone_calls
    WHERE caller = '(367) 555-5533'
    AND year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60);
