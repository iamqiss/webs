// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "WebsApp",
    platforms: [.iOS(.v17)],
    dependencies: [
        // gRPC
        .package(url: "https://github.com/grpc/grpc-swift.git", from: "1.21.0"),
        // TCA — The Composable Architecture
        .package(url: "https://github.com/pointfreeco/swift-composable-architecture.git", from: "1.10.0"),
        // Swift Protobuf
        .package(url: "https://github.com/apple/swift-protobuf.git", from: "1.26.0"),
    ],
    targets: [
        .target(
            name: "WebsApp",
            dependencies: [
                .product(name: "GRPC",                      package: "grpc-swift"),
                .product(name: "ComposableArchitecture",    package: "swift-composable-architecture"),
                .product(name: "SwiftProtobuf",             package: "swift-protobuf"),
            ]
        ),
        .testTarget(
            name: "WebsAppTests",
            dependencies: ["WebsApp"]
        ),
    ]
)
