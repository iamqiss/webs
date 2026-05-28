import Foundation

// Webs DI Container (replace with real environment in production)
struct AppContainer {
    let authService: AuthService
    let apiClient: APIClient
}

extension AppContainer {
    static let live = AppContainer(
        authService: AuthService(),
        apiClient: APIClient()
    )

    static let mock = AppContainer(
        authService: AuthService(),
        apiClient: APIClient()
    )
}
