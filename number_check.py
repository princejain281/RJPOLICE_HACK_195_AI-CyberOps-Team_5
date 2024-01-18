from truecallerpy import search_phonenumber

async def main():
    
    phone_number = input("Enter the phone number (with country code, e.g., +919460******): ")
    
    id = "a1i0O--kQqrCT-ZVJ6u8abQ-tq3L9GbVGCn4VvJAPjrTI24ME3ZIREGjs76sxtY4"

    response = await search_phonenumber(phone_number, "IN", id)

    data = response.get('data', {}).get('data', [])

    for entry in data:
        print(f"Name: {entry.get('name', 'N/A')}")
        print(f"Score: {entry.get('score', 'N/A')}")
        print(f"Phone Number: {phone_number}")
        print(f"Carrier: {entry.get('phones', [{}])[0].get('carrier', 'N/A')}")
        print(f"City: {entry.get('addresses', [{}])[0].get('city', 'N/A')}")
        print("-----")

        
import asyncio
asyncio.run(main())
