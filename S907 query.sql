SELECT
    cast(matnr as CHAR(18)) as DMDUNIT,
    cast(vkorg as CHAR(4)) as SALESORG,
    cast(werks as CHAR(4)) as PLANT,
    cast(plawe as CHAR(2)) as COUNTRYOFORIGIN,
    cast('ORDER' as CHAR(6)) as HISTSTREAM,
    cast(zmeng as CHAR(13)) as QTY,
    cast('1' as CHAR(1)) as TYPE,
    -- the below cast should be changed to cast spmon to char(6) and add
    -- 01 to this to form the date.
    cast(to_date(spmon, 'YYYYMM') as char(8)) as STARTDATE,
    'M' as PERIOD_IND
FROM S907
WHERE vrsio = 'A00' and spmon >= 201610 and spmon <= 201808
