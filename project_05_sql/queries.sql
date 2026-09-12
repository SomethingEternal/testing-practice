-- 1. Простой SELECT: вывести всех актёров
SELECT * FROM actor;

-- 2. WHERE: актёры с именем NICK
SELECT * FROM actor WHERE first_name = 'NICK';

-- 3. LIKE: фильмы, название которых начинается с 'A'
SELECT title FROM film WHERE title LIKE 'A%';

-- 4. COUNT: посчитать количество фильмов
SELECT COUNT(*) FROM film;

-- 5. GROUP BY: количество фильмов для каждого рейтинга
SELECT rating, COUNT(*) FROM film GROUP BY rating;

-- 6. JOIN: вывести фильмы и их языки
SELECT f.title, l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- 7. JOIN + WHERE: вывести клиентов из города 'London'
SELECT c.first_name, c.last_name, a.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
WHERE a.city = 'London';

-- 8. LEFT JOIN: все клиенты и их платежи (включая тех, у кого платежей нет)
SELECT c.first_name, c.last_name, p.amount
FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id;

-- 9. Подзапрос: фильмы дороже среднего
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 10. GROUP BY + HAVING: клиенты, сделавшие больше 30 платежей
SELECT customer_id, COUNT(*) AS payment_count
FROM payment
GROUP BY customer_id
HAVING COUNT(*) > 30;