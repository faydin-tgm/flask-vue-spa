context('Button Tests', () => {
  it('Post Test', () => {
    cy.visit('http://localhost:8080/')
    cy.get('#inputUsername').type('username')
    cy.get('#inputEmail').type('email')
    cy.get('#inputPicture').type('image')
    cy.get('#postButton').click()
  })

})
