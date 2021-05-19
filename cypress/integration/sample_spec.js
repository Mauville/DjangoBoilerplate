describe('Add student', () => {
  it('Successfully adds student', () => {
    cy.visit('localhost:8000');
    cy.get('#nameField').type('Miguel ');
    cy.get('#surnameField').type('Venegas Sanchez');
    cy.get('#cityField').type('CDMX');
    cy.get('#bdate').type('2005-11-23');
    cy.get('#btnsmt').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal(`El estudiante fue creado exitosamente.`);
    });
  });
});

describe('AgeCheck', () => {
  it('Fail to add student because of age', () => {
    cy.visit('localhost:8000');
    cy.get('#nameField').type('Miguel ');
    cy.get('#surnameField').type('Venegas Sanchez');
    cy.get('#cityField').type('CDMX');
    cy.get('#bdate').type('1999-11-23');
    cy.get('#btnsmt').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal(`No se pudo crear un estudiante.

  - El estudiante debe ser menor de 18 años.`);
    });
  });
});
describe('NameCheck', () => {
  it('Fails to add student without name', () => {
    cy.visit('localhost:8000');
    cy.get('#surnameField').type('Venegas Sanchez');
    cy.get('#cityField').type('CDMX');
    cy.get('#bdate').type('2005-11-23');
    cy.get('#btnsmt').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal(`No se pudo crear un estudiante.

  - No puede estar vacio nombres`);
    });
  });
});
describe('CityCheck', () => {
  it('Fail to add student without city', () => {
    cy.visit('localhost:8000');
    cy.get('#nameField').type('Miguel ');
    cy.get('#surnameField').type('Venegas Sanchez');
    cy.get('#bdate').type('2005-11-23');
    cy.get('#btnsmt').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal(`No se pudo crear un estudiante.

  - No puede estar vacio ciudad`);
    });
  });
});
