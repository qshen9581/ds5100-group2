import os
import unittest
import geopandas as gpd

class GDFTest(unittest.TestCase):
   
    def test_for_geometry(self):
        """
        Unit test to check if geopandas dataframe geometry 
        column is in fact a geometry type.

        Returns
        -------
        None.

        """
        fp = os.path.join(os.path.dirname(__file__), r'data\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp')
        test_gdf = gpd.read_file(fp)[['geometry']].to_crs('EPSG:4326')
        sample_gdf = gpd.GeoDataFrame({'geometry': []}, crs="EPSG:4326")
        self.assertEqual(test_gdf['geometry'].dtype, sample_gdf['geometry'].dtype)
        
if __name__ == '__main__':
    unittest.main()