import React, { useState } from "react";

const CustomersList = () => {
  // Using state hook to make content/value to be rendered dynamic/up-to-date
  const [customersCount, setCustomersCount] = useState(10);
  const [customers, setCustomers] = useState([
    {
      id: 1,
      name: "Little Princess",
      contacts: "123-456",
      address: { city: "HeavenHold" },
      image: "https://picsum.photos/id/7/60",
    },
    {
      id: 2,
      name: "Lorraine",
      contacts: null,
      address: { city: "Nairobi" },
      image: "https://picsum.photos/id/999/60",
    },
    {
      id: 3,
      name: "Marrianne",
      contacts: "111-333",
      address: { city: "Lake-Side" },
      image: "https://picsum.photos/id/1014/60",
    },
    {
      id: 4,
      name: "Sohee",
      contacts: "987-654",
      address: { city: "AstroWorld" },
      image: "https://picsum.photos/id/203/60",
    },
    {
      id: 5,
      name: "Plague Doctor",
      contacts: null,
      address: { city: "England-Bro" },
      image: "https://picsum.photos/id/900/60",
    },
  ]);

  // Executes when the user clicks on the Reload button
  const onReloadClick = () => {
    // Update the state for the react to automatically update the Browser DOM
    setCustomersCount(1000);
  };

  // Adding a function to get contacts to render
  const getContactsToRender = (contacts) => {
    if (contacts) return contacts;
    else {
      return (
        <div className="bg-warning p-2 text-center">Contact Not On Display</div>
      );
    }
  };
  // Function to handle changing the picture
  const onChangePictureClick = (index) => {
    let updatedCustomers = [...customers];
    updatedCustomers[index].image = "https://picsum.photos/id/77/60";
    setCustomers(updatedCustomers);
  };

  return (
    <>
      <h4 className="m-2 p-2">
        Customers

        <span className="badge text-bg-secondary m-2">
          {customersCount}
        </span>

        <button className="btn btn-info" onClick={onReloadClick}>
          Reload
        </button>
      </h4>

      <table className="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Picture</th>
            <th>Customer Name</th>
            <th>Contact Info</th>
            <th>City</th>
          </tr>
        </thead>
        <tbody>
          {customers.map((c, index)=> (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>
                <img src={c.image} alt="Mug-Shot" />
                <div>
                  <button
                    className="btn btn-sm btn-secondary"
                    onClick={() => onChangePictureClick(index)}
                  >
                    Change Picture
                  </button>
                </div>
              </td>
              <td>{c.name}</td>
              <td>{getContactsToRender(c.contacts)}</td>
              <td>{c.address.city}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default CustomersList;