INSERT INTO films (title, description, year, rating, file_path, picture_path, is_tvshow) VALUES
('Movie 1', 'Description for Movie 1', 2020, 7.5, '/path/to/movie1.mp4', '/path/to/movie1.jpg', FALSE),
('Movie 2', 'Description for Movie 2', 2021, 8.1, '/path/to/movie2.mp4', '/path/to/movie2.jpg', FALSE),
('Movie 3', 'Description for Movie 3', 2019, 6.3, '/path/to/movie3.mp4', '/path/to/movie3.jpg', FALSE),
('Movie 4', 'Description for Movie 4', 2018, 5.7, '/path/to/movie4.mp4', '/path/to/movie4.jpg', FALSE),
('Movie 5', 'Description for Movie 5', 2022, 9.0, '/path/to/movie5.mp4', '/path/to/movie5.jpg', FALSE),
('Movie 6', 'Description for Movie 6', 2020, 7.2, '/path/to/movie6.mp4', '/path/to/movie6.jpg', FALSE),
('Movie 7', 'Description for Movie 7', 2021, 8.4, '/path/to/movie7.mp4', '/path/to/movie7.jpg', FALSE),
('Movie 8', 'Description for Movie 8', 2017, 6.9, '/path/to/movie8.mp4', '/path/to/movie8.jpg', FALSE),
('Movie 9', 'Description for Movie 9', 2016, 5.8, '/path/to/movie9.mp4', '/path/to/movie9.jpg', FALSE),
('Movie 10', 'Description for Movie 10', 2015, 7.7, '/path/to/movie10.mp4', '/path/to/movie10.jpg', FALSE);

INSERT INTO categories (name) VALUES
('Action'),
('Drama'),
('Comedy'),
('Sci-Fi'),
('Horror');

-- Связать фильмы с категориями
INSERT INTO category_film_association (film_id, category_id) VALUES
(1, 1), -- Movie 1 -> Action
(2, 2), -- Movie 2 -> Drama
(3, 3), -- Movie 3 -> Comedy
(4, 1), -- Movie 4 -> Action
(4, 4), -- Movie 4 -> Sci-Fi
(5, 5), -- Movie 5 -> Horror
(6, 1), -- Movie 6 -> Action
(7, 2), -- Movie 7 -> Drama
(8, 3), -- Movie 8 -> Comedy
(9, 1), -- Movie 9 -> Action
(9, 4), -- Movie 9 -> Sci-Fi
(10, 2), -- Movie 10 -> Drama
(10, 5); -- Movie 10 -> Horror

-- tv_shovs
INSERT INTO films (title, description, year, rating, file_path, picture_path, is_tvshow)
VALUES
    ('The Great Adventure', 'An epic journey across uncharted lands.', 2020, 8.7, '/media/great_adventure.mp4', '/images/great_adventure.jpg', true),
    ('Space Quest', 'A thrilling space opera exploring the farthest reaches of the galaxy.', 2021, 9.1, '/media/space_quest.mp4', '/images/space_quest.jpg', true);

INSERT INTO episodes (title, season, episode, file_path, picture_path, film_id)
VALUES
    ('The Journey Begins', 1, 1, '/media/great_adventure_s01e01.mp4', '/images/great_adventure_s01e01.jpg', 11),
    ('Into the Wild', 1, 2, '/media/great_adventure_s01e02.mp4', '/images/great_adventure_s01e02.jpg', 11),
    ('The Mountain Pass', 2, 1, '/media/great_adventure_s02e01.mp4', '/images/great_adventure_s02e01.jpg', 11);

INSERT INTO episodes (title, season, episode, file_path, picture_path, film_id)
VALUES
    ('The Call to Adventure', 1, 1, '/media/space_quest_s01e01.mp4', '/images/space_quest_s01e01.jpg', 12),
    ('The Dark Frontier', 1, 2, '/media/space_quest_s01e02.mp4', '/images/space_quest_s01e02.jpg', 12),
    ('First Contact', 2, 1, '/media/space_quest_s02e01.mp4', '/images/space_quest_s02e01.jpg', 12),
    ('The Lost Colony', 3, 1, '/media/space_quest_s03e01.mp4', '/images/space_quest_s03e01.jpg', 12);
