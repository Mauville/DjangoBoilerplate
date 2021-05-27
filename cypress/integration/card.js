describe('Passing Check', () => {
    it('should pass on correct data', () => {
        cy.visit('./static/card.html');

        cy.get('#name').type('MIGUEL SANCHEZ ');
        cy.get('#cardNumber').type('4445 5554 44523 1234');
        cy.get('#month').type('12');
        cy.get('#year').type('22');
        cy.get('#cvv').type('123');
        cy.get('#submitbutton').click()
        cy.on("window:load", () => {
            console.log('done')
        })
    });
});

describe('Name Check', () => {
    it('should not redirect on no name', () => {
        cy.visit('./static/card.html');

        cy.get('#cardNumber').type('4445 5554 44523 1234');
        cy.get('#month').type('12');
        cy.get('#year').type('22');
        cy.get('#cvv').type('123');
        cy.get('#submitbutton').click()
        cy.on("window:load", () => {
        })
    });
});
describe('Number Check', () => {
    it('should not redirect on no number', () => {
        cy.visit('./static/card.html');

        cy.get('#name').type('MIGUEL SANCHEZ');
        // cy.get('#cardNumber').type('4445 5554 44523 1234');
        cy.get('#month').type('12');
        cy.get('#year').type('22');
        cy.get('#cvv').type('123');
        cy.get('#submitbutton').click()
        cy.on("window:load", () => {
        })
    });
});
describe('Month Check', () => {
    it('should not redirect on incorrect month', () => {
        cy.visit('./static/card.html');

        cy.get('#name').type('MIGUEL SANCHEZ');
        cy.get('#cardNumber').type('4445 5554 44523 1234');
        cy.get('#month').type('18');
        cy.get('#year').type('22');
        cy.get('#cvv').type('123');
        cy.get('#submitbutton').click()
        cy.on("window:load", () => {
        })
    });
    describe('year Check', () => {
        it('should not redirect on incorrect year', () => {
            cy.visit('./static/card.html');

            cy.get('#name').type('MIGUEL SANCHEZ');
            cy.get('#cardNumber').type('4445 5554 44523 1234');
            cy.get('#month').type('11');
            cy.get('#year').type('18');
            cy.get('#cvv').type('123');
            cy.get('#submitbutton').click()
            cy.on("window:load", () => {
            })
        });
    });
});

describe('cvv Check', () => {
    it('should not redirect on no cvv', () => {
        cy.visit('./static/card.html');

        cy.get('#name').type('MIGUEL SANCHEZ');
        cy.get('#cardNumber').type('4445 5554 44523 1234');
        cy.get('#month').type('11');
        cy.get('#year').type('28');
        cy.get('#submitbutton').click()
        cy.on("window:load", () => {
        })
    });
});
