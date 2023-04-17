Data Cleaning
================
2023-02-27

``` r
# Gives summary of data
sum_full <- summary(New_data[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")])
sum_rep <- summary(Rep_data[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")])
sum_2019 <- summary(Finally_Cleaned_2019_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")])
sum_2020 <- summary(Finally_Cleaned_2020_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS", "NoHomeDesign")])
sum_2021 <- summary(Finally_Cleaned_2021_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")])
sum_2022 <- summary(Finally_Cleaned_2022_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")])

# Finds SD of data
SD_full <- apply(New_data[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")], 2, sd)
SD_rep <- apply(Rep_data[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")], 2, sd)
SD_2019 <- apply(Finally_Cleaned_2019_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")], 2, sd)
SD_2020 <- apply(Finally_Cleaned_2020_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS", "NoHomeDesign")], 2, sd)
SD_2021 <- apply(Finally_Cleaned_2021_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")], 2, sd)
SD_2022 <- apply(Finally_Cleaned_2022_home[c("win.loss", "avg.OPS", "avg.Opp.OPS", "avg.GS", "avg.Opp.GS")], 2, sd)

# Statistics Output
sum_full
```

    ##     win.loss         avg.OPS        avg.Opp.OPS         avg.GS      
    ##  Min.   :0.0000   Min.   :0.4925   Min.   :0.4820   Min.   : 0.400  
    ##  1st Qu.:0.0000   1st Qu.:0.6663   1st Qu.:0.6637   1st Qu.: 3.400  
    ##  Median :1.0000   Median :0.7149   Median :0.7127   Median : 4.200  
    ##  Mean   :0.5365   Mean   :0.7164   Mean   :0.7135   Mean   : 4.431  
    ##  3rd Qu.:1.0000   3rd Qu.:0.7648   3rd Qu.:0.7610   3rd Qu.: 5.400  
    ##  Max.   :1.0000   Max.   :0.9940   Max.   :0.9797   Max.   :13.400  
    ##    avg.Opp.GS    
    ##  Min.   : 0.800  
    ##  1st Qu.: 3.400  
    ##  Median : 4.400  
    ##  Mean   : 4.505  
    ##  3rd Qu.: 5.400  
    ##  Max.   :11.600

``` r
SD_full
```

    ##    win.loss     avg.OPS avg.Opp.OPS      avg.GS  avg.Opp.GS 
    ##  0.49869787  0.07199070  0.07162158  1.53155536  1.50594763

``` r
###
#sum_rep
#SD_rep
###
sum_2019
```

    ##     win.loss         avg.OPS        avg.Opp.OPS         avg.GS      
    ##  Min.   :0.0000   Min.   :0.5299   Min.   :0.5347   Min.   : 0.800  
    ##  1st Qu.:0.0000   1st Qu.:0.6932   1st Qu.:0.6884   1st Qu.: 3.600  
    ##  Median :1.0000   Median :0.7436   Median :0.7387   Median : 4.600  
    ##  Mean   :0.5296   Mean   :0.7430   Mean   :0.7379   Mean   : 4.686  
    ##  3rd Qu.:1.0000   3rd Qu.:0.7935   3rd Qu.:0.7875   3rd Qu.: 5.600  
    ##  Max.   :1.0000   Max.   :0.9575   Max.   :0.9524   Max.   :11.600  
    ##    avg.Opp.GS    
    ##  Min.   : 1.000  
    ##  1st Qu.: 3.600  
    ##  Median : 4.600  
    ##  Mean   : 4.713  
    ##  3rd Qu.: 5.600  
    ##  Max.   :11.400

``` r
SD_2019
```

    ##    win.loss     avg.OPS avg.Opp.OPS      avg.GS  avg.Opp.GS 
    ##  0.49922605  0.07301972  0.07346437  1.58137011  1.55351495

``` r
###
sum_2020
```

    ##     win.loss         avg.OPS        avg.Opp.OPS         avg.GS      
    ##  Min.   :0.0000   Min.   :0.5420   Min.   :0.5435   Min.   : 0.800  
    ##  1st Qu.:0.0000   1st Qu.:0.6771   1st Qu.:0.6653   1st Qu.: 3.400  
    ##  Median :1.0000   Median :0.7238   Median :0.7184   Median : 4.200  
    ##  Mean   :0.5576   Mean   :0.7244   Mean   :0.7196   Mean   : 4.398  
    ##  3rd Qu.:1.0000   3rd Qu.:0.7682   3rd Qu.:0.7674   3rd Qu.: 5.400  
    ##  Max.   :1.0000   Max.   :0.9184   Max.   :0.9478   Max.   :12.200  
    ##    avg.Opp.GS      NoHomeDesign   
    ##  Min.   : 1.000   Min.   :0.0000  
    ##  1st Qu.: 3.600   1st Qu.:0.0000  
    ##  Median : 4.800   Median :0.0000  
    ##  Mean   : 4.772   Mean   :0.0316  
    ##  3rd Qu.: 5.600   3rd Qu.:0.0000  
    ##  Max.   :11.600   Max.   :1.0000

``` r
SD_2020
```

    ##     win.loss      avg.OPS  avg.Opp.OPS       avg.GS   avg.Opp.GS NoHomeDesign 
    ##   0.49695608   0.06869055   0.07334517   1.53030324   1.56318089   0.17503873

``` r
###
sum_2021
```

    ##     win.loss        avg.OPS        avg.Opp.OPS         avg.GS    
    ##  Min.   :0.000   Min.   :0.4953   Min.   :0.4820   Min.   : 0.4  
    ##  1st Qu.:0.000   1st Qu.:0.6651   1st Qu.:0.6654   1st Qu.: 3.4  
    ##  Median :1.000   Median :0.7105   Median :0.7113   Median : 4.2  
    ##  Mean   :0.538   Mean   :0.7119   Mean   :0.7105   Mean   : 4.4  
    ##  3rd Qu.:1.000   3rd Qu.:0.7566   3rd Qu.:0.7558   3rd Qu.: 5.4  
    ##  Max.   :1.000   Max.   :0.9940   Max.   :0.9797   Max.   :10.8  
    ##    avg.Opp.GS   
    ##  Min.   :0.800  
    ##  1st Qu.:3.400  
    ##  Median :4.400  
    ##  Mean   :4.477  
    ##  3rd Qu.:5.400  
    ##  Max.   :9.800

``` r
SD_2021
```

    ##    win.loss     avg.OPS avg.Opp.OPS      avg.GS  avg.Opp.GS 
    ##  0.49866106  0.06659265  0.06527752  1.48528605  1.48176160

``` r
###
sum_2022
```

    ##     win.loss         avg.OPS        avg.Opp.OPS         avg.GS      
    ##  Min.   :0.0000   Min.   :0.4925   Min.   :0.4909   Min.   : 0.600  
    ##  1st Qu.:0.0000   1st Qu.:0.6468   1st Qu.:0.6440   1st Qu.: 3.200  
    ##  Median :1.0000   Median :0.6899   Median :0.6893   Median : 4.200  
    ##  Mean   :0.5342   Mean   :0.6915   Mean   :0.6898   Mean   : 4.219  
    ##  3rd Qu.:1.0000   3rd Qu.:0.7340   3rd Qu.:0.7331   3rd Qu.: 5.200  
    ##  Max.   :1.0000   Max.   :0.9337   Max.   :0.9325   Max.   :13.400  
    ##    avg.Opp.GS   
    ##  Min.   :0.800  
    ##  1st Qu.:3.200  
    ##  Median :4.200  
    ##  Mean   :4.225  
    ##  3rd Qu.:5.200  
    ##  Max.   :9.600

``` r
SD_2022
```

    ##    win.loss     avg.OPS avg.Opp.OPS      avg.GS  avg.Opp.GS 
    ##  0.49893494  0.06772819  0.06679219  1.49099291  1.40854731

``` r
# Simple regression
simp.model <- glm(win.loss ~ season, data = Rep_data )
#summary(simp.model)

# Replication of Losak and Sabel model, logistic regression
rep.model.log <- glm(win.loss ~ season + gameday + gameday*season + NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, data = Rep_data, family = "binomial")
summary(rep.model.log)
```

    ## 
    ## Call:
    ## glm(formula = win.loss ~ season + gameday + gameday * season + 
    ##     NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, 
    ##     family = "binomial", data = Rep_data)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -2.4648  -1.0332   0.5232   0.9870   2.5985  
    ## 
    ## Coefficients:
    ##                  Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)     0.8850414  0.5559487   1.592   0.1114    
    ## season         -0.2118175  0.1750240  -1.210   0.2262    
    ## gameday         0.0002445  0.0009720   0.252   0.8014    
    ## NoHomeDesign   -1.0070363  0.4264790  -2.361   0.0182 *  
    ## avg.GS         -0.4148275  0.0276079 -15.026  < 2e-16 ***
    ## avg.Opp.GS      0.3353137  0.0278284  12.049  < 2e-16 ***
    ## avg.OPS         2.9361063  0.5646434   5.200 1.99e-07 ***
    ## avg.Opp.OPS    -3.5027743  0.5405615  -6.480 9.18e-11 ***
    ## season:gameday  0.0080939  0.0044201   1.831   0.0671 .  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 4558.0  on 3300  degrees of freedom
    ## Residual deviance: 3929.9  on 3292  degrees of freedom
    ## AIC: 3947.9
    ## 
    ## Number of Fisher Scoring iterations: 3

``` r
# Replication of Losak and Sabel model
rep.model <- glm(win.loss ~ season + gameday + gameday*season + NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, data = Rep_data)
summary(rep.model)
```

    ## 
    ## Call:
    ## glm(formula = win.loss ~ season + gameday + gameday * season + 
    ##     NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, 
    ##     data = Rep_data)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -1.1061  -0.4287   0.1170   0.4026   1.1817  
    ## 
    ## Coefficients:
    ##                  Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)     6.991e-01  1.147e-01   6.098 1.20e-09 ***
    ## season         -4.585e-02  3.660e-02  -1.253   0.2104    
    ## gameday         2.652e-05  2.005e-04   0.132   0.8948    
    ## NoHomeDesign   -2.133e-01  8.744e-02  -2.440   0.0147 *  
    ## avg.GS         -8.423e-02  5.181e-03 -16.259  < 2e-16 ***
    ## avg.Opp.GS      6.693e-02  5.336e-03  12.544  < 2e-16 ***
    ## avg.OPS         6.073e-01  1.159e-01   5.240 1.71e-07 ***
    ## avg.Opp.OPS    -7.368e-01  1.110e-01  -6.639 3.68e-11 ***
    ## season:gameday  1.675e-03  9.148e-04   1.831   0.0671 .  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for gaussian family taken to be 0.2063239)
    ## 
    ##     Null deviance: 820.70  on 3300  degrees of freedom
    ## Residual deviance: 679.22  on 3292  degrees of freedom
    ## AIC: 4168.8
    ## 
    ## Number of Fisher Scoring iterations: 2

``` r
# Simple regression
simp.model <- glm(win.loss ~ season, data = New_data )
#summary(simp.model)

# Replication of Losak and Sabel model, logistic regression
rep.model.log <- glm(win.loss ~ s.2020 + s.2021 + s.2022 + gameday + gameday*season + NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, data = New_data, family = "binomial")
summary(rep.model.log)
```

    ## 
    ## Call:
    ## glm(formula = win.loss ~ s.2020 + s.2021 + s.2022 + gameday + 
    ##     gameday * season + NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + 
    ##     avg.Opp.OPS, family = "binomial", data = New_data)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -2.4641  -1.0325   0.5142   0.9832   2.6063  
    ## 
    ## Coefficients: (1 not defined because of singularities)
    ##                  Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)     0.2906407  0.3858234   0.753   0.4513    
    ## s.2020          0.0217297  0.1060135   0.205   0.8376    
    ## s.2021         -0.0226629  0.0976009  -0.232   0.8164    
    ## s.2022         -0.0465826  0.1285840  -0.362   0.7171    
    ## gameday        -0.5278924  0.9013093  -0.586   0.5581    
    ## season                 NA         NA      NA       NA    
    ## NoHomeDesign   -0.9752280  0.4248769  -2.295   0.0217 *  
    ## avg.GS         -0.4302330  0.0182459 -23.580  < 2e-16 ***
    ## avg.Opp.GS      0.3889065  0.0185006  21.021  < 2e-16 ***
    ## avg.OPS         2.9198194  0.3745284   7.796 6.39e-15 ***
    ## avg.Opp.OPS    -2.8982122  0.3722878  -7.785 6.98e-15 ***
    ## gameday:season  0.0002615  0.0004460   0.586   0.5577    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 11223.1  on 8126  degrees of freedom
    ## Residual deviance:  9650.6  on 8116  degrees of freedom
    ## AIC: 9672.6
    ## 
    ## Number of Fisher Scoring iterations: 3

``` r
# Replication of Losak and Sabel model
rep.model. <- glm(win.loss ~ s.2020 + s.2021 + s.2022 + gameday + gameday*season + NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, data = New_data)
summary(rep.model)
```

    ## 
    ## Call:
    ## glm(formula = win.loss ~ season + gameday + gameday * season + 
    ##     NoHomeDesign + avg.GS + avg.Opp.GS + avg.OPS + avg.Opp.OPS, 
    ##     data = Rep_data)
    ## 
    ## Deviance Residuals: 
    ##     Min       1Q   Median       3Q      Max  
    ## -1.1061  -0.4287   0.1170   0.4026   1.1817  
    ## 
    ## Coefficients:
    ##                  Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)     6.991e-01  1.147e-01   6.098 1.20e-09 ***
    ## season         -4.585e-02  3.660e-02  -1.253   0.2104    
    ## gameday         2.652e-05  2.005e-04   0.132   0.8948    
    ## NoHomeDesign   -2.133e-01  8.744e-02  -2.440   0.0147 *  
    ## avg.GS         -8.423e-02  5.181e-03 -16.259  < 2e-16 ***
    ## avg.Opp.GS      6.693e-02  5.336e-03  12.544  < 2e-16 ***
    ## avg.OPS         6.073e-01  1.159e-01   5.240 1.71e-07 ***
    ## avg.Opp.OPS    -7.368e-01  1.110e-01  -6.639 3.68e-11 ***
    ## season:gameday  1.675e-03  9.148e-04   1.831   0.0671 .  
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for gaussian family taken to be 0.2063239)
    ## 
    ##     Null deviance: 820.70  on 3300  degrees of freedom
    ## Residual deviance: 679.22  on 3292  degrees of freedom
    ## AIC: 4168.8
    ## 
    ## Number of Fisher Scoring iterations: 2

  
