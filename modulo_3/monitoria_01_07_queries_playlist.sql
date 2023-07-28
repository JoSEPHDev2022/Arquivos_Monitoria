-- Exiba o nome do gênero e a média de tempo das musicas em milisegundos agrupadas
-- por gênero
SELECT
	Genre.Name AS "Gênero Musical",
	ROUND(AVG(Track.Milliseconds)) AS "Média de Duração (milisegundos)"
FROM
	Genre
LEFT JOIN
	Track ON Genre.GenreId = Track.GenreId
GROUP BY
	"Gênero Musical"
ORDER BY
	"Média de Duração (milisegundos)" DESC;
	
-- Exiba o álbum que possui a maior média de tempo em milisegundos 
-- cujo gênero musical é Rock;
SELECT
	Album.Title AS "Album",
	ROUND(AVG(Track.Milliseconds)) AS "Média de Duração (milisegundos)",
	Genre.Name AS "Gênero Musical"
FROM
	Album
LEFT JOIN
	Track ON Album.AlbumId = Track.AlbumId
LEFT JOIN
	Genre ON Genre.GenreId = Track.GenreId
WHERE
	Genre.Name = 'Rock'
GROUP BY
	"Album", "Gênero Musical"
ORDER BY
	"Média de Duração (milisegundos)" DESC;


-- Selecione o nome das playlists e o total de músicas (Track.Name) agrupadas pelas
-- playlists que pertencem e ordenadas pelas playlists que possuem mais músicas;
SELECT
	pl.Name AS "Nome da Playlist",
	COUNT(Track.Name) AS "Quantidade de Músicas"
FROM
	Playlist AS pl
LEFT JOIN
	PlaylistTrack AS pt ON pl.PlaylistId = pt.PlaylistId
LEFT JOIN
	Track ON pt.TrackId = Track.TrackId
GROUP BY
	"Nome da Playlist"
ORDER BY
	"Quantidade de Músicas" DESC;
