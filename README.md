# kinometer

## Usage

The following endpoints are supported:

* https://kinometer.gagnonagon.com - random sorting
* https://kinometer.gagnonagon.com/bg - sorting on Brian's scores (desc)
* https://kinometer.gagnonagon.com/jw - sorting on Josh's scores (desc)
* https://kinometer.gagnonagon.com/title - sorts on title
* https://kinometer.gagnonagon.com/year - sorts on release year

Add the query parameter `?order=asc` to reverse the order.
* https://kinometer.gagnonagon.com/title?order=asc

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Adding Media

Adding media to the kinometer is achieved in 5 steps. 

1. Add an object in the below form to [movies.json](./asset_loader/data/movies.json), [tv_shows.json](./asset_loader/data/tv_shows.json), or [games.json](./asset_loader/data/games.json). 
    ```json
    {
        "title": "Raw",
        "releaseYear": 2016,
        "moviePath": "Raw (2016)",
        "score1": "8.65",
        "score2": "7.81"
    }
    ```

2. Run [load_movies.py](./asset_loader/load_movies.py) or [load_tv_shows.py](./asset_loader/load_tv_shows.py). Preferably select for only added elements to avoid reloading all images. I'm too lazy to deal with this differently right now. 

3. Run [load_db_file.py](./asset_loader/load_db_file.py). This refreshes the "database" of movie data supporting the front-end. 

4. Build the app with npm:
    ```sh
    npm run build
    ```

5. Run an `aws s3 sync` command, excluding all other assets except the added media. 
    ```sh
    aws s3 sync dist/ s3://bgagnon-kinometer-bucket --profile admin --exclude 'assets/movies/*' --include 'assets/movies/Raw (2016)/*'
    ```

6. Optionally, invalidation cloudfront to expire the old cached site. 
    ```sh
    aws cloudfront create-invalidation --distribution-id E3CWZOKXLPK4SM --paths "/*" --profile admin
    ```

## Deploy

```sh
/usr/local/bin/sam/sam deploy --s3-bucket sam-resources-bucket --profile admin
```

```sh
aws s3 sync dist/ s3://bgagnon-kinometer-bucket --profile admin --exclude 'assets/movies/*'
```

```sh
aws cloudfront create-invalidation --distribution-id E3CWZOKXLPK4SM --paths "/*" --profile admin
```

## TOOD:

* **Switch to Terraform**. To my shame, this site is using SAM and CloudFormation instead of Terraform. I have ready-made examples for hosting spa in S3, this was just the fastest way for me to get things working. 
* **Remove duplicate code across MovieSplash and PosterSplash components**. I added the solution for PosterSplash last minute. It's basically all copy paste. Not an issue if I don't ever plan on touching those components again. But would be nice to clean up. 
