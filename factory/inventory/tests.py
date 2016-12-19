from django.test import TestCase
from django.db import IntegrityError
from models import Manufacturer, InventoryItem
from rest_framework.test import APITestCase
from rest_framework import status


class ManufacturerTestCase(TestCase):
    def setUp(self):
        self.alpha = Manufacturer.objects.create(
            name="Alpha",
            address="123 Apple Ave., Region, Country",
            phone="1234567890"
        )

        self.zulu = Manufacturer.objects.create(
            name="Zulu",
            address="987 Zebra Lane, Region, Country",
            phone="111234567890"
        )

    def test_create_items(self):
        """
        Test that items can be created, given valid manufacturers
        """

        self.adze = InventoryItem.objects.create(
            name="adze",
            manufacturer=self.alpha,
            description="apple handled adze",
            size="0.1,0.02,0.04",  # units are in meters
            weight=".45",  # units are in kg
            unit_of_issue="each",
            quantity=7
        )

        self.zip_ties = InventoryItem.objects.create(
            name="zip ties",
            manufacturer=self.zulu,
            description="pack of zip ties",
            size="0.04,0.04,0.12",  # units are in meters
            weight="1.1",  # units are in kg
            unit_of_issue="box of 100",
            quantity=23
        )

        self.assertEqual(self.adze.quantity, 7)
        self.assertEqual(self.zip_ties.quantity, 23)
        self.assertEqual(self.adze.manufacturer, self.alpha)
        self.assertEqual(self.zip_ties.manufacturer, self.zulu)

    def test_missing_manufacturer(self):
        """
        Check that an instance can't be created without a manufacturer
        """

        with self.assertRaises(IntegrityError):

            InventoryItem.objects.create(
                name="anvil",
                description="apple handled adze",
                size="0.1,0.02,0.04",  # units are in meters
                weight=".45",  # units are in kg
                unit_of_issue="each",
                quantity=7
            )


class AccountTests(APITestCase):

    def setUp(self):
        """
        set up some new data for follow up tests
        """
        url = '/inventory/manufacturers/'
        data = dict(name="Agile",
                    address="123 Apple Ave., Region, Country",
                    phone="1234567890")
        self.client.post(url, data, format='json')


        url = '/inventory/items/'
        data = dict(manufacturer=Manufacturer.objects.get().id,
                    name="one",
                    description="item one",
                    size="0.1,0.02,0.04",
                    weight=".45",
                    unit_of_issue="each",
                    quantity=8
                )

        self.client.post(url, data, format='json')

    def test_read_manufacturer(self):
        """
        Tests the creation of an manufacturer via the REST API.
        """
        self.assertEqual(Manufacturer.objects.count(), 1)
        self.assertEqual(Manufacturer.objects.get().name, 'Agile')

    def test_create_and_delete_manufacturer(self):
        """
        Tests the creation and deletion of a manufacturer via the REST API.
        """
        url = '/inventory/manufacturers/'
        data = dict(name="Bauble",
                    address="234, Bee Lane",
                    phone="5654890351")
        response = self.client.post(url, data, format='json')

        # check that the new manufacturer was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Manufacturer.objects.count(), 2)

        # delete that new manufacturer and check that it worked
        response = self.client.delete(url + '2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Manufacturer.objects.count(), 1)

    def test_update_item(self):
        """
        Test that we can update an existing inventory item
        """
        # get an item from the test database
        one = InventoryItem.objects.filter(name='one').get()

        # build its URL
        url = '/inventory/items/{}/'.format(one.id)

        # enter a new quantity for updating the inventory item
        data = dict(quantity='22')

        # send and HTTP PATCH request for updating the item
        response = self.client.patch(url, data, format='json')

        # verify the status code and the update
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(InventoryItem.objects.filter(name='one').get().quantity, 22)

