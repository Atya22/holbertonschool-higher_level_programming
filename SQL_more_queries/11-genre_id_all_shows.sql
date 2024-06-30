-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL for shows without genres.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.`title`, tv_show_genres.`genre_id`
  FROM `tv_shows`
       LEFT JOIN `tv_show_genres`
       ON tv_shows.`id` = tv_show_genres.`show_id`
 ORDER BY tv_shows.`title`, tv_show_genres.`genre_id`;