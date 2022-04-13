
import os
import unittest
import pycountry
import geopandas as gpd

class GDFTest(unittest.TestCase):
   
    def test_for_geometry(self):
        """
        Unit test to check if geopandas dataframe geometry 
        column is in fact a geopandas geometry data dtype type.

        Returns
        -------
        None.

        """
        
        fp = os.path.join(os.path.dirname(__file__), r'data\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp')
        test_gdf = gpd.read_file(fp)[['geometry']].to_crs('EPSG:4326')
        
        sample_gdf = gpd.GeoDataFrame({'geometry': []}, crs="EPSG:4326")
        self.assertEqual(test_gdf['geometry'].dtype, sample_gdf['geometry'].dtype)
        
    def test_country_info(self):
        """
        Unit test to check if the country codes and the names match as expected
        
        Returns
        -------
        None.

        """
        country_dat = {'Germany': 'DEU', 'United States': 'USA', 'Italy': 'ITA', 'Australia': 'AUS'}
        
        for country_name, country_code in country_dat.items():
            result = pycountry.countries.get(alpha_3=country_code)
            result.name
            self.assertTrue(country_name==result.name, f'Expected name {country_name} does not match {result.name}')
    
if __name__ == '__main__':
    unittest.main()
